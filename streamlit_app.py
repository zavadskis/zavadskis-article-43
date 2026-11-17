import streamlit as st
st.set_page_config(page_title=open("title.txt").read().strip(), layout="centered")
st.markdown(open("article.md", encoding="utf-8").read(), unsafe_allow_html=True)
