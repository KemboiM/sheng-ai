import pandas as pd
from src.data.clean_data import clean_dataframe


def test_clean_dataframe_normalizes_and_deduplicates():
    df = pd.DataFrame([
        {"record_id": 1, "sheng": " NIAJE ", "swahili": "habari", "english": "what's up", "meaning": "greeting", "category": "greeting", "source_name": "test", "permission_basis": "original", "training_use_allowed": "yes", "commercial_use_allowed": "yes", "review_status": "reviewed"},
        {"record_id": 2, "sheng": "niaje", "swahili": "habari", "english": "what's up", "meaning": "greeting", "category": "greeting", "source_name": "test", "permission_basis": "original", "training_use_allowed": "yes", "commercial_use_allowed": "yes", "review_status": "reviewed"},
    ])
    out = clean_dataframe(df)
    assert len(out) == 1
    assert out.loc[0, "sheng"] == "niaje"
