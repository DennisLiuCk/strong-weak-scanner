#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""建立與離線驗證質化研究的內容定址 evidence pack。

本工具不下載來源。Drafter 先把 3-5 份核心 PDF 放在本機，再以 build 建立
不可覆寫的 pack；reviewer 使用 verify 重算文件與 pack SHA，不必重新下載。
render 只處理引用頁及其前後一頁。
"""

import argparse
import hashlib
import json
import os
import re
import shutil
import stat
import struct
import subprocess
import sys
import tempfile
import unicodedata
import zlib
from datetime import datetime
from pathlib import Path
from urllib.parse import urlsplit, urlunsplit

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass


ROOT = Path(__file__).resolve().parent.parent
DEFAULT_PACK_ROOT = ROOT / "tmp" / "qualitative_evidence" / "packs"
DEFAULT_MANIFEST_ROOT = ROOT / "notes" / "qualitative" / "evidence"
SCHEMA = "findmind.qual-evidence-pack"
SCHEMA_VERSION = 1
RESEARCH_PROFILE = "focused_v1"
SOURCE_SEARCH_TIMEOUT_MINUTES = 10
MIN_CORE_SOURCES = 3
MAX_CORE_SOURCES = 5
SOURCE_ID_RE = re.compile(r"S[1-9]\d*")
SHA256_RE = re.compile(r"[0-9a-f]{64}")
REQUIRED_CORE_ROLES = (
    "annual_report",
    "annual_financials",
    "latest_quarterly_report",
    "latest_investor_conference",
)
OPTIONAL_CORE_ROLES = ("shareholder_meeting",)
ALLOWED_CORE_ROLES = REQUIRED_CORE_ROLES + OPTIONAL_CORE_ROLES
_WRITE_BITS = stat.S_IWUSR | stat.S_IWGRP | stat.S_IWOTH


class EvidenceError(ValueError):
    """輸入、schema 或完整性契約失敗。"""


def _sha256_file(path):
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _resolve_executable(value):
    executable = shutil.which(str(value)) or str(Path(value).expanduser().resolve())
    if not Path(executable).is_file():
        raise EvidenceError(f"找不到外部工具：{value}")
    return executable


def _pdf_page_count(path, pdfinfo="pdfinfo", timeout_seconds=30):
    """用 Poppler 驗證 PDF 可解析，並回傳實際實體頁數。"""
    executable = _resolve_executable(pdfinfo)
    creationflags = getattr(subprocess, "CREATE_NO_WINDOW", 0) if os.name == "nt" else 0
    environment = os.environ.copy()
    environment.update({"LC_ALL": "C", "LANG": "C"})
    try:
        completed = subprocess.run(
            [executable, str(path)],
            shell=False,
            check=True,
            timeout=timeout_seconds,
            creationflags=creationflags,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding="utf-8",
            errors="replace",
            env=environment,
        )
    except (OSError, subprocess.CalledProcessError, subprocess.TimeoutExpired) as exc:
        raise EvidenceError(f"PDF 無法由 pdfinfo 解析：{path}") from exc
    match = re.search(r"^Pages:\s+(\d+)\s*$", completed.stdout, re.M)
    if not match or int(match.group(1)) < 1:
        raise EvidenceError(f"pdfinfo 未回傳合法頁數：{path}")
    return int(match.group(1))


def _valid_png(path):
    """以 stdlib 驗證 PNG 結構、CRC、非零尺寸與必要 chunks。"""
    try:
        payload = Path(path).read_bytes()
    except OSError:
        return False
    if len(payload) < 45 or payload[:8] != b"\x89PNG\r\n\x1a\n":
        return False
    offset, first, saw_idat = 8, True, False
    while offset + 12 <= len(payload):
        length = struct.unpack(">I", payload[offset:offset + 4])[0]
        end = offset + 12 + length
        if end > len(payload):
            return False
        chunk_type = payload[offset + 4:offset + 8]
        chunk_data = payload[offset + 8:offset + 8 + length]
        expected_crc = struct.unpack(">I", payload[offset + 8 + length:end])[0]
        if zlib.crc32(chunk_type + chunk_data) & 0xFFFFFFFF != expected_crc:
            return False
        if first:
            if chunk_type != b"IHDR" or length != 13:
                return False
            width, height = struct.unpack(">II", chunk_data[:8])
            if width < 1 or height < 1:
                return False
            first = False
        if chunk_type == b"IDAT":
            saw_idat = True
        if chunk_type == b"IEND":
            return length == 0 and saw_idat and end == len(payload)
        offset = end
    return False


def _canonical_string(value):
    return unicodedata.normalize("NFC", str(value))


def _canonical_url(value):
    value = _canonical_string(value)
    if any(character.isspace() for character in value):
        raise EvidenceError("來源 URL 不可含空白")
    parsed = urlsplit(value)
    if parsed.scheme.lower() != "https" or not parsed.hostname:
        raise EvidenceError("來源 URL 必須是完整 HTTPS URL")
    if parsed.username is not None or parsed.password is not None or parsed.fragment:
        raise EvidenceError("來源 URL 不可含帳密或 fragment")
    try:
        port = parsed.port
    except ValueError as exc:
        raise EvidenceError("來源 URL port 不合法") from exc
    hostname = parsed.hostname.rstrip(".").encode("idna").decode("ascii").lower()
    if ":" in hostname:
        hostname = f"[{hostname}]"
    netloc = hostname if port in (None, 443) else f"{hostname}:{port}"
    return urlunsplit(("https", netloc, parsed.path, parsed.query, ""))


def _canonical_payload(manifest):
    documents = []
    for document in sorted(manifest.get("documents", []), key=lambda item: int(item["id"][1:])):
        documents.append({
            "id": document["id"],
            "roles": sorted(document["roles"], key=ALLOWED_CORE_ROLES.index),
            "url": _canonical_string(document["url"]),
            "file": document["file"],
            "sha256": document["sha256"],
            "size_bytes": document["size_bytes"],
            "page_count": document["page_count"],
            "cited_pages": list(document["cited_pages"]),
        })
    return {
        "schema": manifest.get("schema"),
        "schema_version": manifest.get("schema_version"),
        "research_profile": manifest.get("research_profile"),
        "stock_id": manifest.get("stock_id"),
        "content_as_of": manifest.get("content_as_of"),
        "source_search_timeout_minutes": manifest.get("source_search_timeout_minutes"),
        "unverified_claims_removed": manifest.get("unverified_claims_removed"),
        "documents": documents,
    }


def manifest_digest(manifest):
    payload = json.dumps(
        _canonical_payload(manifest),
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
        allow_nan=False,
    ).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def parse_pages(value):
    """把 1-based 頁碼規格如 3-5,9 轉成排序後整數。"""
    pages = set()
    for token in (part.strip() for part in (value or "").split(",")):
        if not token:
            continue
        if "-" in token:
            first_text, last_text = token.split("-", 1)
            if not first_text.isdigit() or not last_text.isdigit():
                raise EvidenceError(f"頁碼範圍格式錯誤：{token}")
            first, last = int(first_text), int(last_text)
        else:
            if not token.isdigit():
                raise EvidenceError(f"頁碼格式錯誤：{token}")
            first = last = int(token)
        if first < 1 or last < first:
            raise EvidenceError(f"頁碼範圍不合法：{token}")
        pages.update(range(first, last + 1))
    if not pages:
        raise EvidenceError("每份核心 PDF 都必須明列實際引用頁")
    return sorted(pages)


def expanded_render_pages(cited_pages, page_count, margin=1):
    pages = set()
    for page in cited_pages:
        pages.update(range(max(1, page - margin), min(page_count, page + margin) + 1))
    return sorted(pages)


def collapse_ranges(pages):
    values = sorted(set(pages))
    if not values:
        return []
    ranges, first, last = [], values[0], values[0]
    for page in values[1:]:
        if page == last + 1:
            last = page
            continue
        ranges.append({"first": first, "last": last})
        first = last = page
    ranges.append({"first": first, "last": last})
    return ranges


def _parse_mapping(items, option_name):
    result = {}
    for raw in items or []:
        key, separator, value = raw.partition("=")
        if not separator or not SOURCE_ID_RE.fullmatch(key) or not value:
            raise EvidenceError(f"{option_name} 必須使用 S1=值 格式：{raw}")
        if key in result:
            raise EvidenceError(f"{option_name} 重複定義：{key}")
        result[key] = value
    return result


def parse_roles(value):
    roles = [item.strip() for item in (value or "").split(",") if item.strip()]
    if not roles or len(roles) != len(set(roles)):
        raise EvidenceError("每份核心文件必須有不重複的 role")
    unknown = sorted(set(roles) - set(ALLOWED_CORE_ROLES))
    if unknown:
        raise EvidenceError("未知核心文件 role：" + ", ".join(unknown))
    if len(roles) > 1 and set(roles) != {"annual_report", "annual_financials"}:
        raise EvidenceError("只有同一 PDF 的 annual_report 與 annual_financials 可合併")
    return sorted(roles, key=ALLOWED_CORE_ROLES.index)


def _role_errors(documents):
    errors = []
    counts = {role: 0 for role in ALLOWED_CORE_ROLES}
    for document in documents:
        if not isinstance(document, dict):
            continue
        roles = document.get("roles")
        if (not isinstance(roles, list) or not roles
                or any(not isinstance(role, str) for role in roles)
                or len(roles) != len(set(roles))
                or any(role not in ALLOWED_CORE_ROLES for role in roles)):
            errors.append(f"{document.get('id', '?')} roles 不合法")
            continue
        if len(roles) > 1 and set(roles) != {"annual_report", "annual_financials"}:
            errors.append(f"{document.get('id', '?')} 只能合併年報與年度財報角色")
        for role in roles:
            counts[role] += 1
    for role in REQUIRED_CORE_ROLES:
        if counts[role] != 1:
            errors.append(f"核心文件 role {role} 必須剛好出現一次")
    if counts["shareholder_meeting"] > 1:
        errors.append("shareholder_meeting 最多只能有一份")
    return errors


def _is_linklike(path):
    path = Path(path)
    is_junction = getattr(path, "is_junction", None)
    return path.is_symlink() or bool(is_junction and is_junction())


def _is_read_only(path):
    return not (stat.S_IMODE(Path(path).stat().st_mode) & _WRITE_BITS)


def _seal_pack(pack_dir):
    """封存 SHA payload；渲染圖另存 pack 外，不會再改動這棵目錄。"""
    pack_dir = Path(pack_dir)
    for path in sorted(pack_dir.rglob("*"), key=lambda item: len(item.parts), reverse=True):
        if path.is_file():
            os.chmod(path, stat.S_IRUSR | stat.S_IRGRP | stat.S_IROTH)
        elif path.is_dir():
            os.chmod(path, stat.S_IRUSR | stat.S_IXUSR | stat.S_IRGRP | stat.S_IXGRP
                     | stat.S_IROTH | stat.S_IXOTH)
    os.chmod(pack_dir, stat.S_IRUSR | stat.S_IXUSR | stat.S_IRGRP | stat.S_IXGRP
             | stat.S_IROTH | stat.S_IXOTH)


def _discard_tree(path, allowed_root):
    path = Path(path).resolve()
    allowed_root = Path(allowed_root).resolve()
    try:
        inside = os.path.commonpath([str(allowed_root), str(path)]) == str(allowed_root)
    except ValueError:
        inside = False
    if not inside or path == allowed_root:
        raise EvidenceError(f"拒絕清除非預期目錄：{path}")
    if not path.exists():
        return
    for item in path.rglob("*"):
        try:
            os.chmod(item, stat.S_IRUSR | stat.S_IWUSR | (stat.S_IXUSR if item.is_dir() else 0))
        except OSError:
            pass
    try:
        os.chmod(path, stat.S_IRUSR | stat.S_IWUSR | stat.S_IXUSR)
    except OSError:
        pass
    shutil.rmtree(path)


def _render_output_dir(pack_dir, manifest, render_root=None):
    pack_dir = Path(pack_dir).resolve()
    root = Path(render_root).resolve() if render_root else pack_dir.parent / "renders"
    pack_id = str(manifest.get("pack_sha256") or "invalid-pack")
    return root / pack_id


def _safe_local_source(path):
    candidate = Path(path).expanduser()
    if _is_linklike(candidate):
        raise EvidenceError(f"來源不是一般檔案：{path}")
    source = candidate.resolve()
    if not source.is_file():
        raise EvidenceError(f"來源不是一般檔案：{path}")
    with open(source, "rb") as handle:
        if handle.read(5) != b"%PDF-":
            raise EvidenceError(f"核心文件不是 PDF：{path}")
    return source


def _write_json_new_or_same(path, manifest):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    content = json.dumps(manifest, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    if path.exists():
        if path.read_text(encoding="utf-8") != content:
            raise EvidenceError(f"不覆寫既有不同 manifest：{path}")
        return
    descriptor, temporary_name = tempfile.mkstemp(
        prefix=f".{path.name}.", suffix=".tmp", dir=path.parent
    )
    os.close(descriptor)
    temporary = Path(temporary_name)
    try:
        temporary.write_text(content, encoding="utf-8", newline="\n")
        try:
            os.link(temporary, path)
        except FileExistsError:
            if path.read_text(encoding="utf-8") != content:
                raise EvidenceError(f"不覆寫競態建立的不同 manifest：{path}")
    finally:
        temporary.unlink(missing_ok=True)


def _validate_build_inputs(stock_id, content_as_of, sources, urls, pages, page_counts, roles):
    if not re.fullmatch(r"\d{4}", stock_id or ""):
        raise EvidenceError("stock_id 必須是四位數字")
    try:
        parsed_date = datetime.strptime(content_as_of, "%Y-%m-%d")
        if parsed_date.strftime("%Y-%m-%d") != content_as_of:
            raise ValueError
    except ValueError as exc:
        raise EvidenceError("content_as_of 必須是合法 YYYY-MM-DD") from exc
    ids = set(sources)
    if not MIN_CORE_SOURCES <= len(ids) <= MAX_CORE_SOURCES:
        raise EvidenceError("focused_v1 必須使用 3-5 份核心文件")
    for label, mapping in (
        ("--url", urls), ("--pages", pages), ("--page-count", page_counts), ("--role", roles)
    ):
        if set(mapping) != ids:
            raise EvidenceError(f"{label} 的來源 ID 必須與 --source 完全一致")
    role_documents = [
        {"id": source_id, "roles": parse_roles(roles[source_id])}
        for source_id in sorted(ids, key=lambda value: int(value[1:]))
    ]
    role_errors = _role_errors(role_documents)
    if role_errors:
        raise EvidenceError("；".join(role_errors))


def build_pack(
    stock_id,
    content_as_of,
    sources,
    urls,
    pages,
    page_counts,
    roles,
    pdfinfo="pdfinfo",
    pack_root=DEFAULT_PACK_ROOT,
    manifest_out=None,
):
    """複製核心 PDF、建立內容定址 pack，並輸出可提交的小型 manifest。"""
    _validate_build_inputs(stock_id, content_as_of, sources, urls, pages, page_counts, roles)
    prepared = []
    for source_id in sorted(sources, key=lambda value: int(value[1:])):
        source = _safe_local_source(sources[source_id])
        try:
            url = _canonical_url(urls[source_id])
        except EvidenceError as exc:
            raise EvidenceError(f"{source_id} 來源 URL 不合法：{exc}") from exc
        try:
            page_count = int(page_counts[source_id])
        except ValueError as exc:
            raise EvidenceError(f"{source_id} page-count 必須是正整數") from exc
        if page_count < 1:
            raise EvidenceError(f"{source_id} page-count 必須是正整數")
        actual_page_count = _pdf_page_count(source, pdfinfo=pdfinfo)
        if page_count != actual_page_count:
            raise EvidenceError(
                f"{source_id} page-count {page_count} 與 PDF 實際 {actual_page_count} 不一致"
            )
        cited_pages = parse_pages(pages[source_id])
        if cited_pages[-1] > page_count:
            raise EvidenceError(f"{source_id} 引用頁超過 PDF 頁數 {page_count}")
        prepared.append(
            (source_id, source, url, page_count, cited_pages, parse_roles(roles[source_id]))
        )

    pack_root = Path(pack_root).resolve()
    stock_root = pack_root / stock_id
    stock_root.mkdir(parents=True, exist_ok=True)
    staging = Path(tempfile.mkdtemp(prefix=".building-", dir=stock_root))
    try:
        documents_dir = staging / "documents"
        documents_dir.mkdir()
        documents = []
        for source_id, source, url, page_count, cited_pages, source_roles in prepared:
            destination = documents_dir / f"{source_id}.pdf"
            shutil.copyfile(source, destination)
            documents.append({
                "id": source_id,
                "roles": source_roles,
                "url": url,
                "file": f"documents/{source_id}.pdf",
                "sha256": _sha256_file(destination),
                "size_bytes": destination.stat().st_size,
                "page_count": page_count,
                "cited_pages": cited_pages,
                "rendered_pages": expanded_render_pages(cited_pages, page_count),
            })
        manifest = {
            "schema": SCHEMA,
            "schema_version": SCHEMA_VERSION,
            "research_profile": RESEARCH_PROFILE,
            "stock_id": stock_id,
            "content_as_of": content_as_of,
            "source_search_timeout_minutes": SOURCE_SEARCH_TIMEOUT_MINUTES,
            "unverified_claims_removed": True,
            "documents": documents,
        }
        manifest["pack_sha256"] = manifest_digest(manifest)
        manifest_errors = validate_manifest(manifest)
        if manifest_errors:
            raise EvidenceError("；".join(manifest_errors))
        final_pack = stock_root / manifest["pack_sha256"]
        if final_pack.exists():
            existing, errors = verify_pack(final_pack, pdfinfo=pdfinfo)
            if errors or existing.get("pack_sha256") != manifest["pack_sha256"]:
                raise EvidenceError(f"既有內容定址 pack 驗證失敗：{final_pack}")
            # 完全相同的 bytes／來源／頁面／角色沿用既有 immutable pack。
            manifest = existing
        else:
            _write_json_new_or_same(staging / "manifest.json", manifest)
            _seal_pack(staging)
            moved = False
            try:
                os.replace(staging, final_pack)
                moved = True
            except OSError:
                if not final_pack.exists():
                    raise
                existing, final_errors = verify_pack(final_pack, pdfinfo=pdfinfo)
                if final_errors or existing.get("pack_sha256") != manifest["pack_sha256"]:
                    raise EvidenceError(f"競態建立的 pack 驗證失敗：{final_pack}")
                manifest = existing
            if moved:
                try:
                    _, final_errors = verify_pack(final_pack, pdfinfo=pdfinfo)
                    if final_errors:
                        raise EvidenceError("；".join(final_errors))
                except Exception:
                    _discard_tree(final_pack, allowed_root=stock_root)
                    raise
    finally:
        _discard_tree(staging, allowed_root=stock_root)

    if manifest_out is None:
        manifest_out = (
            DEFAULT_MANIFEST_ROOT / stock_id
            / f"{content_as_of}_{manifest['pack_sha256'][:16]}.json"
        )
    _write_json_new_or_same(manifest_out, manifest)
    return manifest, final_pack, Path(manifest_out).resolve()


def load_manifest(path):
    try:
        manifest = json.loads(Path(path).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise EvidenceError(f"manifest 無法讀取：{path}") from exc
    if not isinstance(manifest, dict):
        raise EvidenceError("manifest 根節點必須是 JSON object")
    return manifest


def validate_manifest(manifest):
    """只驗證可提交 manifest；不接觸本機 PDF。"""
    errors = []
    if not isinstance(manifest, dict):
        return ["evidence manifest 根節點必須是 JSON object"]
    allowed_root = {
        "schema", "schema_version", "research_profile", "stock_id", "content_as_of",
        "source_search_timeout_minutes", "unverified_claims_removed",
        "documents", "pack_sha256",
    }
    if set(manifest) - allowed_root:
        errors.append("evidence manifest 含未納入 SHA 契約的未知欄位")
    if manifest.get("schema") != SCHEMA or manifest.get("schema_version") != SCHEMA_VERSION:
        errors.append("evidence manifest schema 不支援")
    if manifest.get("research_profile") != RESEARCH_PROFILE:
        errors.append("evidence manifest research_profile 必須是 focused_v1")
    if not re.fullmatch(r"\d{4}", str(manifest.get("stock_id", ""))):
        errors.append("evidence manifest stock_id 不合法")
    try:
        content_as_of = str(manifest.get("content_as_of", ""))
        parsed_date = datetime.strptime(content_as_of, "%Y-%m-%d")
        if parsed_date.strftime("%Y-%m-%d") != content_as_of:
            raise ValueError
    except ValueError:
        errors.append("evidence manifest content_as_of 不合法")
    if manifest.get("source_search_timeout_minutes") != SOURCE_SEARCH_TIMEOUT_MINUTES:
        errors.append("來源追查預算必須固定為 10 分鐘")
    if manifest.get("unverified_claims_removed") is not True:
        errors.append("manifest 必須證明未驗證主張已從正文移除")
    documents = manifest.get("documents")
    if not isinstance(documents, list) or not MIN_CORE_SOURCES <= len(documents) <= MAX_CORE_SOURCES:
        errors.append("evidence manifest 必須有 3-5 份核心文件")
        documents = documents if isinstance(documents, list) else []
    seen = set()
    seen_urls = set()
    seen_hashes = set()
    for document in documents:
        source_id = document.get("id") if isinstance(document, dict) else None
        if not SOURCE_ID_RE.fullmatch(str(source_id or "")) or source_id in seen:
            errors.append("evidence manifest 來源 ID 非法或重複")
            continue
        seen.add(source_id)
        allowed_document = {
            "id", "roles", "url", "file", "sha256", "size_bytes", "page_count",
            "cited_pages", "rendered_pages",
        }
        if set(document) - allowed_document:
            errors.append(f"{source_id} 含未納入 SHA 契約的未知欄位")
        try:
            canonical_url = _canonical_url(document.get("url", ""))
        except EvidenceError:
            canonical_url = None
            errors.append(f"{source_id} manifest URL 必須是 canonical HTTPS URL")
        if canonical_url is not None and canonical_url != document.get("url"):
            errors.append(f"{source_id} manifest URL 未正規化")
        elif canonical_url in seen_urls:
            errors.append(f"{source_id} 與其他核心文件使用重複 URL")
        elif canonical_url is not None:
            seen_urls.add(canonical_url)
        filename = str(document.get("file", ""))
        if filename != f"documents/{source_id}.pdf":
            errors.append(f"{source_id} manifest file 路徑不合法")
        if not SHA256_RE.fullmatch(str(document.get("sha256", ""))):
            errors.append(f"{source_id} 文件 SHA-256 不合法")
        elif document["sha256"] in seen_hashes:
            errors.append(f"{source_id} 與其他核心文件內容重複")
        else:
            seen_hashes.add(document["sha256"])
        if type(document.get("size_bytes")) is not int or document["size_bytes"] < 1:
            errors.append(f"{source_id} size_bytes 不合法")
        page_count = document.get("page_count")
        cited = document.get("cited_pages")
        rendered = document.get("rendered_pages")
        if type(page_count) is not int or page_count < 1:
            errors.append(f"{source_id} page_count 不合法")
            continue
        if (not isinstance(cited, list) or not cited
                or any(type(page) is not int or page < 1 or page > page_count for page in cited)
                or cited != sorted(set(cited))):
            errors.append(f"{source_id} cited_pages 不合法")
            continue
        expected = expanded_render_pages(cited, page_count)
        if rendered != expected:
            errors.append(f"{source_id} rendered_pages 必須等於引用頁及前後一頁")
    errors.extend(_role_errors(documents))
    if not SHA256_RE.fullmatch(str(manifest.get("pack_sha256", ""))):
        errors.append("evidence manifest pack_sha256 不合法")
    expected_digest = manifest_digest(manifest) if not errors else None
    if expected_digest and manifest.get("pack_sha256") != expected_digest:
        errors.append("evidence manifest pack_sha256 不一致")
    return errors


def verify_pack(pack_dir, require_renders=False, render_root=None, pdfinfo="pdfinfo"):
    """完全離線驗證 pack；絕不修復或下載來源。"""
    candidate = Path(pack_dir).expanduser()
    if _is_linklike(candidate) or not candidate.is_dir():
        raise EvidenceError(f"pack 不是一般目錄：{pack_dir}")
    pack_dir = candidate.resolve()
    manifest_path = pack_dir / "manifest.json"
    if _is_linklike(manifest_path) or not manifest_path.is_file():
        raise EvidenceError("pack 缺少一般檔案 manifest.json")
    manifest = load_manifest(manifest_path)
    errors = validate_manifest(manifest)
    if pack_dir.name != manifest.get("pack_sha256"):
        errors.append("pack 目錄名必須等於完整 pack_sha256")
    if pack_dir.parent.name != manifest.get("stock_id"):
        errors.append("pack 必須位於對應 stock_id 子目錄")
    if not _is_read_only(pack_dir):
        errors.append("evidence pack 根目錄仍可寫入")
    if not _is_read_only(manifest_path):
        errors.append("evidence manifest 仍可寫入")
    actual_root = {item.name for item in pack_dir.iterdir()}
    if actual_root != {"documents", "manifest.json"}:
        errors.append("evidence pack 根目錄含未列入契約的項目")

    documents_dir = pack_dir / "documents"
    if (_is_linklike(documents_dir) or not documents_dir.is_dir()
            or not _is_read_only(documents_dir)):
        errors.append("documents 必須是唯讀的一般目錄")
    if errors:
        return manifest, errors
    expected_files = set()
    documents = manifest.get("documents", [])
    if not isinstance(documents, list):
        documents = []
    for document in documents:
        if not isinstance(document, dict):
            continue
        source_id = document.get("id")
        if not SOURCE_ID_RE.fullmatch(str(source_id or "")):
            continue
        relative = Path(document.get("file", ""))
        raw_file_path = pack_dir / relative
        file_path = raw_file_path.resolve()
        try:
            if os.path.commonpath([str(pack_dir), str(file_path)]) != str(pack_dir):
                raise ValueError
        except ValueError:
            errors.append(f"{source_id} 文件路徑逃出 pack")
            continue
        expected_files.add(file_path)
        if not file_path.is_file() or _is_linklike(raw_file_path):
            errors.append(f"{source_id} 文件缺失或不是一般檔案")
            continue
        if not _is_read_only(file_path):
            errors.append(f"{source_id} 文件仍可寫入")
        with open(file_path, "rb") as handle:
            if handle.read(5) != b"%PDF-":
                errors.append(f"{source_id} 文件不是 PDF")
        try:
            actual_page_count = _pdf_page_count(file_path, pdfinfo=pdfinfo)
            if actual_page_count != document.get("page_count"):
                errors.append(f"{source_id} PDF 實際頁數與 manifest 不一致")
        except EvidenceError as exc:
            errors.append(str(exc))
        if file_path.stat().st_size != document.get("size_bytes"):
            errors.append(f"{source_id} 文件大小不一致")
        if _sha256_file(file_path) != document.get("sha256"):
            errors.append(f"{source_id} 文件 SHA-256 不一致")
    if documents_dir.is_dir():
        actual_entries = list(documents_dir.iterdir())
        expected_names = {path.name for path in expected_files}
        if {item.name for item in actual_entries} != expected_names:
            errors.append("documents 目錄含 manifest 未列項目或缺檔")
        if any(not item.is_file() or _is_linklike(item) for item in actual_entries):
            errors.append("documents 目錄只能包含非連結的一般檔案")
    if require_renders:
        output_dir = _render_output_dir(pack_dir, manifest, render_root=render_root)
        expected_renders = {
            output_dir / document["id"] / f"p-{page:04d}.png"
            for document in documents if isinstance(document, dict) and "id" in document
            for page in document.get("rendered_pages", [])
        }
        actual_renders = {
            item.resolve() for item in output_dir.rglob("*") if item.is_file()
        } if output_dir.is_dir() and not _is_linklike(output_dir) else set()
        missing = [path for path in expected_renders if not path.is_file()]
        if missing:
            errors.append(f"缺少 {len(missing)} 張引用頁渲染圖")
        if actual_renders != {path.resolve() for path in expected_renders}:
            errors.append("渲染目錄含計畫外檔案或缺檔")
        for path in expected_renders:
            if path.is_file() and not _valid_png(path):
                errors.append(f"渲染輸出不是完整 PNG：{path.name}")
    return manifest, errors


def render_plan(manifest):
    return {
        "pack_sha256": manifest["pack_sha256"],
        "margin": 1,
        "documents": [
            {
                "id": document["id"],
                "input": document["file"],
                "ranges": collapse_ranges(document["rendered_pages"]),
            }
            for document in manifest["documents"]
        ],
    }


def render_pack(
    pack_dir,
    pdftoppm="pdftoppm",
    dpi=170,
    timeout_seconds=120,
    render_root=None,
    pdfinfo="pdfinfo",
):
    manifest, errors = verify_pack(pack_dir, pdfinfo=pdfinfo)
    if errors:
        raise EvidenceError("；".join(errors))
    if not 72 <= dpi <= 600 or timeout_seconds < 1:
        raise EvidenceError("dpi 必須為 72–600，timeout 必須大於 0")
    executable = _resolve_executable(pdftoppm)
    pack_dir = Path(pack_dir).resolve()
    render_dir = _render_output_dir(pack_dir, manifest, render_root=render_root)
    try:
        if os.path.commonpath([str(pack_dir), str(render_dir.resolve())]) == str(pack_dir):
            raise EvidenceError("渲染輸出必須位於唯讀 evidence pack 之外")
    except ValueError:
        pass
    if render_dir.exists() and _is_linklike(render_dir):
        raise EvidenceError("渲染輸出目錄不可為 symlink 或 junction")
    creationflags = getattr(subprocess, "CREATE_NO_WINDOW", 0) if os.name == "nt" else 0
    for document in manifest["documents"]:
        source = pack_dir / document["file"]
        output_dir = render_dir / document["id"]
        if output_dir.exists() and _is_linklike(output_dir):
            raise EvidenceError(f"{document['id']} 渲染目錄不可為 symlink 或 junction")
        output_dir.mkdir(parents=True, exist_ok=True)
        for page in document["rendered_pages"]:
            prefix = output_dir / f"p-{page:04d}"
            subprocess.run(
                [
                    executable, "-png", "-singlefile", "-r", str(dpi),
                    "-f", str(page), "-l", str(page), str(source), str(prefix),
                ],
                shell=False,
                check=True,
                timeout=timeout_seconds,
                creationflags=creationflags,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.PIPE,
            )
    _, errors = verify_pack(
        pack_dir, require_renders=True, render_root=render_root, pdfinfo=pdfinfo
    )
    if errors:
        raise EvidenceError("；".join(errors))
    plan = render_plan(manifest)
    plan["render_dir"] = str(render_dir)
    return plan


def _build_command(args):
    sources = _parse_mapping(args.source, "--source")
    urls = _parse_mapping(args.url, "--url")
    pages = _parse_mapping(args.pages, "--pages")
    page_counts = _parse_mapping(args.page_count, "--page-count")
    roles = _parse_mapping(args.role, "--role")
    manifest, pack_dir, manifest_path = build_pack(
        args.stock_id,
        args.content_as_of,
        sources,
        urls,
        pages,
        page_counts,
        roles,
        pdfinfo=args.pdfinfo,
        pack_root=args.out_root,
        manifest_out=args.manifest_out,
    )
    print(json.dumps({
        "pack_sha256": manifest["pack_sha256"],
        "pack_dir": str(pack_dir),
        "manifest": str(manifest_path),
    }, ensure_ascii=False))


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.strip().splitlines()[0])
    subparsers = parser.add_subparsers(dest="command", required=True)

    build = subparsers.add_parser("build", help="由 3-5 份本機核心 PDF 建立 pack")
    build.add_argument("--stock-id", required=True)
    build.add_argument("--content-as-of", required=True)
    build.add_argument("--source", action="append", required=True, help="S1=本機PDF")
    build.add_argument("--url", action="append", required=True, help="S1=https://直接來源")
    build.add_argument("--pages", action="append", required=True, help="S1=3-5,9（PDF實體頁）")
    build.add_argument("--page-count", action="append", required=True, help="S1=總頁數")
    build.add_argument(
        "--role", action="append", required=True,
        help="S1=annual_report,annual_financials",
    )
    build.add_argument("--pdfinfo", default="pdfinfo", help="Poppler pdfinfo 路徑")
    build.add_argument("--out-root", default=str(DEFAULT_PACK_ROOT))
    build.add_argument("--manifest-out")
    build.set_defaults(func=_build_command)

    verify = subparsers.add_parser("verify", help="完全離線重算 pack SHA 與文件 SHA")
    verify.add_argument("pack")
    verify.add_argument("--renders", action="store_true", help="同時要求所有引用頁轉圖存在")
    verify.add_argument("--render-root", help="自訂 pack 外的衍生轉圖根目錄")
    verify.add_argument("--pdfinfo", default="pdfinfo", help="Poppler pdfinfo 路徑")

    plan = subparsers.add_parser("render-plan", help="輸出引用頁及前後一頁的渲染計畫")
    plan.add_argument("pack")
    plan.add_argument("--pdfinfo", default="pdfinfo", help="Poppler pdfinfo 路徑")

    render = subparsers.add_parser("render", help="用 Poppler 只渲染計畫中的頁面")
    render.add_argument("pack")
    render.add_argument("--pdftoppm", default="pdftoppm")
    render.add_argument("--dpi", type=int, default=170)
    render.add_argument("--render-root", help="自訂 pack 外的衍生轉圖根目錄")
    render.add_argument("--pdfinfo", default="pdfinfo", help="Poppler pdfinfo 路徑")

    args = parser.parse_args(argv)
    try:
        if args.command == "verify":
            manifest, errors = verify_pack(
                args.pack,
                require_renders=args.renders,
                render_root=args.render_root,
                pdfinfo=args.pdfinfo,
            )
            for error in errors:
                print(f"ERROR\t{error}", file=sys.stderr)
            if errors:
                return 1
            print(manifest["pack_sha256"])
            return 0
        if args.command == "render-plan":
            manifest, errors = verify_pack(args.pack, pdfinfo=args.pdfinfo)
            if errors:
                raise EvidenceError("；".join(errors))
            print(json.dumps(render_plan(manifest), ensure_ascii=False, indent=2))
            return 0
        if args.command == "render":
            plan_data = render_pack(
                args.pack,
                pdftoppm=args.pdftoppm,
                dpi=args.dpi,
                render_root=args.render_root,
                pdfinfo=args.pdfinfo,
            )
            print(json.dumps(plan_data, ensure_ascii=False, indent=2))
            return 0
        args.func(args)
        return 0
    except EvidenceError as exc:
        print(f"ERROR\t{exc}", file=sys.stderr)
        return 2
    except subprocess.CalledProcessError as exc:
        print(f"ERROR\tPDF 渲染失敗：{exc}", file=sys.stderr)
        return 4
    except subprocess.TimeoutExpired as exc:
        print(f"ERROR\tPDF 渲染逾時：{exc}", file=sys.stderr)
        return 4
    except OSError as exc:
        print(f"ERROR\t檔案或 PDF 工具操作失敗：{exc}", file=sys.stderr)
        return 5


if __name__ == "__main__":
    raise SystemExit(main())
