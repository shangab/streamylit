import streamlit as st
import ModSidebar
import ModOpenAI
import ModML
import ModBI
import ModHuggingface
import ModHome

st.set_page_config(layout="wide")

with open('assets/css/styles.css') as css:
    st.markdown(f'<style>{css.read()}</style>', unsafe_allow_html=True)


ModSidebar.show()

if st.session_state.page == "🏠 Home":
    ModHome.show()

if st.session_state.page == "🤗 HF Transformrs":
    ModHuggingface.show()

if st.session_state.page == "🧠 GPT-3 Completions":
    ModOpenAI.completions()

if st.session_state.page == "🧠 GPT-3 Classification":
    ModOpenAI.classification()

if st.session_state.page == "🧠 GPT-3 Summarization":
    ModOpenAI.summarization()

if st.session_state.page == "🧠 GPT-3 Image Generation":
    ModOpenAI.image()

if st.session_state.page == "💹 BI Sales Dashboard":
    ModBI.sales()
