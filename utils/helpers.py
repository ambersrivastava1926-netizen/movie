import pandas as pd
from pathlib import Path
from datetime import date

BASE_DIR = Path(__file__).resolve().parent.parent

def load_players():
    return pd.read_csv(
        BASE_DIR / "data" / "players.csv",
        encoding="latin1",
        sep=None,              # auto-detect delimiter
        engine="python",       # more tolerant than C engine
        on_bad_lines="skip"    # skip malformed rows
    )

def calculate_age(dob):
    dob = pd.to_datetime(dob, errors="coerce").date()
    today = date.today()
    if pd.isna(dob):
        return "N/A"
    return today.year - dob.year - (
        (today.month, today.day) < (dob.month, dob.day)
    )
