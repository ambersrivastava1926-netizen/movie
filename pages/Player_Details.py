import streamlit as st
from utils.helpers import load_players, calculate_age

st.title("📊 Player Details")

df = load_players()
player_name = st.selectbox("Select Player", df["name"])

player = df[df["name"] == player_name].iloc[0]

st.subheader(player["name"])
st.write("Sport:", player["sport"])
st.write("Country:", player["country"])
st.write("Age:", calculate_age(player["dob"]))
st.write("Matches:", player["matches"])

if player["sport"] == "Cricket":
    st.write("Runs:", player["runs"])
else:
    st.write("Goals:", player["goals"])
