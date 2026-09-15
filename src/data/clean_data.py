from __future__ import annotations

from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[2]
DEFAULT_INPUT = ROOT / "data" / "processed" / "sheng_dictionary.csv"
DEFAULT_OUTPUT = ROOT / "data" / "processed" / "sheng_dictionary_clean.csv"

REQUIRED_COLUMNS = {
    "record_id", "sheng", "swahili", "english", "meaning", "category",
    "source_name", "permission_basis", "training_use_allowed",
    "commercial_use_allowed", "review_status",
}


def clean_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    missing = REQUIRED_COLUMNS.difference(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")

    result = df.copy()
    text_cols = result.select_dtypes(include="object").columns
    for col in text_cols:
        result[col] = result[col].fillna("").astype(str).str.strip()

    result["sheng"] = result["sheng"].str.lower()
    result = result[result["sheng"] != ""]
    result = result.drop_duplicates(subset=["sheng", "meaning"], keep="first")

    allowed = {"yes", "no", "tbd"}
    for col in ["training_use_allowed", "commercial_use_allowed"]:
        invalid = ~result[col].str.lower().isin(allowed)
        if invalid.any():
            bad = sorted(result.loc[invalid, col].unique())
            raise ValueError(f"Invalid values in {col}: {bad}. Use yes/no/tbd.")
        result[col] = result[col].str.lower()

    return result.sort_values(["category", "sheng"]).reset_index(drop=True)


def main(input_path: Path = DEFAULT_INPUT, output_path: Path = DEFAULT_OUTPUT) -> None:
    df = pd.read_csv(input_path)
    cleaned = clean_dataframe(df)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    cleaned.to_csv(output_path, index=False)
    print(f"Cleaned {len(df)} rows -> {len(cleaned)} rows: {output_path}")


if __name__ == "__main__":
    main()
