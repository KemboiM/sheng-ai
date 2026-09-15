from __future__ import annotations

import re
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[2]
LEXICON = ROOT / "data" / "processed" / "sheng_dictionary_clean.csv"
FALLBACK_LEXICON = ROOT / "data" / "processed" / "sheng_dictionary.csv"


def _load_lexicon(path: Path | None = None) -> pd.DataFrame:
    path = path or (LEXICON if LEXICON.exists() else FALLBACK_LEXICON)
    return pd.read_csv(path).fillna("")


def lookup(term: str, target: str = "english", path: Path | None = None) -> dict | None:
    if target not in {"english", "swahili"}:
        raise ValueError("target must be 'english' or 'swahili'")
    df = _load_lexicon(path)
    match = df[df["sheng"].str.lower() == term.strip().lower()]
    if match.empty:
        return None
    row = match.iloc[0].to_dict()
    return {
        "sheng": row["sheng"],
        "translation": row[target],
        "meaning": row["meaning"],
        "example": row.get(f"example_{target}", ""),
        "review_status": row.get("review_status", ""),
    }


def translate_tokens(text: str, target: str = "english", path: Path | None = None) -> str:
    """Naive word-level baseline used only as an MVP benchmark."""
    if target not in {"english", "swahili"}:
        raise ValueError("target must be 'english' or 'swahili'")
    df = _load_lexicon(path)
    mapping = {
        str(row.sheng).lower(): str(getattr(row, target))
        for row in df.itertuples(index=False)
        if str(row.sheng).strip()
    }
    tokens = re.findall(r"\w+|[^\w\s]", text, flags=re.UNICODE)
    out: list[str] = []
    for token in tokens:
        repl = mapping.get(token.lower(), token)
        if token[:1].isupper() and repl:
            repl = repl[:1].upper() + repl[1:]
        out.append(repl)
    result = " ".join(out)
    result = re.sub(r"\s+([?.!,;:])", r"\1", result)
    return result
