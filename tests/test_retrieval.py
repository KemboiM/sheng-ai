from src.rag.retrieval import ShengRetriever


def test_retrieval_finds_rada():
    r = ShengRetriever()
    results = r.search("what does rada mean", top_k=3)
    assert any(item["sheng"] == "rada" for item in results)
