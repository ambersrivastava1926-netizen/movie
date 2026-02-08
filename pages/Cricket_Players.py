import streamlit as st
from utils.helpers import load_players, calculate_age

st.title("🏏 Cricket Players")

df = load_players()
cricket = df[df["sport"] == "Cricket"]

search = st.text_input("Search Player")

if search:
    cricket = cricket[cricket["name"].str.contains(search, case=False)]

for _, p in cricket.iterrows():
    with st.container(border=True):
        st.subheader(p["name"])
        st.write("Country:", p["country"])
        st.write("Age:", calculate_age(p["dob"]))
        st.write("Runs:", p["runs"])
        st.write("Matches:", p["matches"])
