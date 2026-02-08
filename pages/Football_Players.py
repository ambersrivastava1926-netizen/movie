import streamlit as st
from utils.helpers import load_players, calculate_age

st.title("⚽ Football Players")

df = load_players()
football = df[df["sport"] == "Football"]

for _, p in football.iterrows():
    with st.container(border=True):
        st.subheader(p["name"])
        st.write("Country:", p["country"])
        st.write("Age:", calculate_age(p["dob"]))
        st.write("Goals:", p["goals"])
        st.write("Matches:", p["matches"])
