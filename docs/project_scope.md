# Project Scope

## MVP question
Can a small, rights-aware Sheng corpus plus an existing multilingual model provide useful Sheng ↔ Swahili ↔ English translation and conversational assistance, with basic speech interaction?

## In scope
- curated Sheng lexicon and phrase corpus
- provenance/rights metadata
- deterministic baseline translator
- retrieval-augmented generation (RAG) interface
- adapter layer for a multilingual LLM
- speech-to-text prototype
- text-to-speech prototype
- Streamlit demo
- controlled Scripture translation-assistant workflow
- tests and evaluation set

## Out of scope for the 18-day MVP
- training a foundation model from scratch
- mass unauthorized scraping
- publishing a complete Bible translation
- cloning creator voices without explicit rights
- production-grade mobile deployment

## Success criteria
- 300+ verified lexicon/phrase records by Day 10
- 100-item held-out evaluation set
- usable translation demo for common conversational Sheng
- working speech input/output pipeline on at least 20 test recordings
- complete provenance and rights fields for all retained data
