import streamlit as st
import sidebar
import gpt3
import ml
import bi
import hf
import home

st.set_page_config(layout="wide")

with open('assets/css/styles.css') as css:
    st.markdown(f'<style>{css.read()}</style>', unsafe_allow_html=True)


sidebar.show()

if st.session_state.page == "🏠 Home":
    home.show()

if st.session_state.page == "🤗 HF Transformrs":
    hf.show()
    hf.show2()

if st.session_state.page == "🧠 GPT-3 Completions":
    gpt3.completions()

if st.session_state.page == "🧠 GPT-3 Classification":
    gpt3.classification()

if st.session_state.page == "🧠 GPT-3 Summarization":
    gpt3.summarization()

if st.session_state.page == "🧠 GPT-3 Image Generation":
    gpt3.image()

if st.session_state.page == "💹 BI Sales Dashboard":
    bi.sales()
