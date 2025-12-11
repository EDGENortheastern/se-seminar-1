import streamlit as st
from format_name import make_pretty_name

st.title("Pretty Hello App")

name = st.text_input("Enter your name:")

if name:
    st.markdown(make_pretty_name(name))
