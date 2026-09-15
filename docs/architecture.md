# Architecture

```text
Text / Speech
     |
     +--> Speech-to-Text (when audio)
     |
Normalization / language identification
     |
Lexicon retrieval (RAG)
     |
Multilingual LLM adapter
     |
Safety + provenance-aware response layer
     |
Text response
     |
     +--> Text-to-Speech (optional)
```

## Data path

```text
Authorized sources
  -> raw/local staging
  -> cleaning + normalization
  -> rights/provenance validation
  -> human review
  -> processed corpus
  -> retrieval/evaluation/fine-tuning experiments
```
