import streamlit as st

st.title("My First Streamlit App")

st.write("Hello 👋 This is a simple Streamlit example.")

name = st.text_input("Enter your name")

if name:
    st.success(f"Welcome, {name}!")

value = st.slider("Select a number", 0, 100, 50)
st.write("Selected value:", value)

