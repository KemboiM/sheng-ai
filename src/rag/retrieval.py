from __future__ import annotations

from pathlib import Path
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

ROOT = Path(__file__).resolve().parents[2]
DEFAULT_LEXICON = ROOT / "data" / "processed" / "sheng_dictionary_clean.csv"
FALLBACK_LEXICON = ROOT / "data" / "processed" / "sheng_dictionary.csv"


class ShengRetriever:
    def __init__(self, path: Path | None = None):
        path = path or (DEFAULT_LEXICON if DEFAULT_LEXICON.exists() else FALLBACK_LEXICON)
        self.df = pd.read_csv(path).fillna("")
        self.documents = self.df.apply(
            lambda r: " | ".join(
                [
                    str(r["sheng"]), str(r["swahili"]), str(r["english"]),
                    str(r["meaning"]), str(r["example_sheng"]), str(r["category"]),
                ]
            ),
            axis=1,
        ).tolist()
        self.vectorizer = TfidfVectorizer(ngram_range=(1, 2), analyzer="word")
        self.matrix = self.vectorizer.fit_transform(self.documents)

    def search(self, query: str, top_k: int = 5) -> list[dict]:
        q = self.vectorizer.transform([query])
        scores = cosine_similarity(q, self.matrix).ravel()
        indexes = scores.argsort()[::-1][:top_k]
        results: list[dict] = []
        for idx in indexes:
            row = self.df.iloc[idx].to_dict()
            row["score"] = float(scores[idx])
            results.append(row)
        return results

    def context(self, query: str, top_k: int = 5) -> str:
        rows = self.search(query, top_k=top_k)
        return "\n".join(
            f"- {r['sheng']}: English={r['english']}; Swahili={r['swahili']}; "
            f"Meaning={r['meaning']}; Example={r['example_sheng']}"
            for r in rows
            if r["score"] > 0
        )
