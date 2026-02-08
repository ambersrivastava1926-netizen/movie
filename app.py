import streamlit as st
from utils.helpers import load_players

st.set_page_config(page_title="Player Stats", layout="wide")

st.title("🏆 Player Stats Website")
st.subheader("Track top Cricket & Football players")

players = load_players()

col1, col2 = st.columns(2)
with col1:
    st.metric("Total Players", len(players))
with col2:
    st.metric("Sports Covered", players["sport"].nunique())

st.markdown("---")
st.dataframe(players[["name", "sport", "country", "matches"]], use_container_width=True)


