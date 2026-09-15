from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import streamlit as st
from src.translation.baseline import lookup, translate_tokens
from src.rag.retrieval import ShengRetriever
from src.translation.llm_adapter import ShengLLMAdapter

st.set_page_config(page_title="Sheng AI MVP", page_icon="🗣️", layout="centered")
st.title("Sheng AI MVP")
st.caption("Sheng ↔ Swahili ↔ English • rights-aware language prototype")

mode = st.radio("Mode", ["Translate", "Explain slang", "RAG context"], horizontal=True)
text = st.text_input("Enter Sheng text", value="Rada ya leo ni gani?")
target = st.selectbox("Target language", ["English", "Swahili"])

if st.button("Run", type="primary") and text.strip():
    if mode == "Translate":
        result = translate_tokens(text, target.lower())
        st.subheader("Baseline result")
        st.write(result)
        adapter = ShengLLMAdapter()
        prompt = adapter.build_prompt(text, target)
        with st.expander("LLM-ready prompt (Day 7/8)"):
            st.code(prompt.system + "\n\n" + prompt.user)
    elif mode == "Explain slang":
        result = lookup(text.strip().lower(), target.lower())
        if result:
            st.json(result)
        else:
            st.warning("No exact term found in the current seed lexicon.")
    else:
        retriever = ShengRetriever()
        st.dataframe(retriever.search(text, top_k=5), use_container_width=True)

st.divider()
st.info("Seed entries are marked for native-speaker review. Social-platform scraping is not enabled in this MVP.")
