from __future__ import annotations

from dataclasses import dataclass
from src.rag.retrieval import ShengRetriever


@dataclass
class TranslationPrompt:
    system: str
    user: str


class ShengLLMAdapter:
    """Provider-neutral prompt builder.

    Day 7/8 integrates a chosen model provider. Keeping provider calls outside
    this class lets us swap a local Hugging Face model, an API, or a fine-tuned
    adapter without rewriting the product.
    """

    def __init__(self, retriever: ShengRetriever | None = None):
        self.retriever = retriever or ShengRetriever()

    def build_prompt(self, text: str, target_language: str = "English") -> TranslationPrompt:
        context = self.retriever.context(text, top_k=5)
        system = (
            "You are Sheng AI, a Kenyan language assistant. Translate naturally rather than "
            "word-for-word. Sheng is code-switched and context-sensitive. Use only the supplied "
            "lexicon context when it is relevant; do not invent definitions. When uncertain, say so."
        )
        user = (
            f"Target language: {target_language}\n"
            f"Input: {text}\n\n"
            f"Verified/curated lexicon context:\n{context or '(no matching entry)'}\n\n"
            "Return a natural translation and one short note for any slang term that materially affects meaning."
        )
        return TranslationPrompt(system=system, user=user)
