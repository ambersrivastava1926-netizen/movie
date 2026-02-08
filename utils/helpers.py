import pandas as pd
from pathlib import Path
from datetime import date

BASE_DIR = Path(__file__).resolve().parent.parent

def load_players():
    df = pd.read_csv(
        BASE_DIR / "data" / "players.csv",
        encoding="latin1",
        sep=None,
        engine="python",
        on_bad_lines="skip"
    )

    # Normalize column names
    df.columns = (
        df.columns
        .astype(str)
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )

    return df


def calculate_age(dob):
    dob = pd.to_datetime(dob, errors="coerce")
    if pd.isna(dob):
        return "N/A"

    today = date.today()
    return today.year - dob.year - (
        (today.month, today.day) < (dob.month, dob.day)
    )
