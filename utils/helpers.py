import pandas as pd
from pathlib import Path
from datetime import date

BASE_DIR = Path(__file__).resolve().parent.parent

def load_players():
    return pd.read_csv(BASE_DIR / "data" / "players.csv")

def calculate_age(dob):
    dob = pd.to_datetime(dob).date()
    today = date.today()
    return today.year - dob.year - (
        (today.month, today.day) < (dob.month, dob.day)
    )
