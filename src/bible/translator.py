from __future__ import annotations

from dataclasses import dataclass


@dataclass
class ScriptureDraft:
    reference: str
    source_translation: str
    source_text: str
    sheng_draft: str
    reviewer: str = ""
    status: str = "draft"
    rights_basis: str = "UNVERIFIED"


def validate_for_publication(record: ScriptureDraft) -> tuple[bool, list[str]]:
    issues: list[str] = []
    if record.rights_basis in {"", "UNVERIFIED"}:
        issues.append("Source-text rights/permission have not been verified.")
    if not record.reviewer.strip():
        issues.append("Human linguistic/theological review is required.")
    if record.status.lower() not in {"reviewed", "approved"}:
        issues.append("Draft is not marked reviewed/approved.")
    return (not issues, issues)
