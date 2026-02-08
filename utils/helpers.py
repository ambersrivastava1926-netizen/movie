import pandas as pd
from datetime import date

def load_players():
    return pd.read_csv("data/players.csv")

def calculate_age(dob):
    dob = pd.to_datetime(dob).date()
    today = date.today()
    return today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
