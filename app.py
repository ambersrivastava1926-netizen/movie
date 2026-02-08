import streamlit as st
from utils.helpers import load_players

st.set_page_config(
    page_title="Player Stats",
    layout="wide"
)

st.title("Track top Cricket & Football players")

players = load_players()

st.metric("Total Players", len(players))

if "sport" in players.columns:
    st.metric("Sports Covered", players["sport"].nunique())
else:
    st.warning("⚠️ Column 'sport' not found in CSV")

st.markdown("### Player Data Preview")
st.dataframe(players.head(), use_container_width=True)
