from src.translation.baseline import lookup, translate_tokens


def test_lookup_known_term():
    result = lookup("niaje")
    assert result is not None
    assert "what" in result["translation"].lower()


def test_baseline_replaces_known_token():
    result = translate_tokens("Niaje buda?", "english")
    assert "What's up" in result
    assert "bro" in result.lower()
