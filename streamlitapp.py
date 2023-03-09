import streamlit as st
import sidebar
import gpt3
import ml

with open('assets/css/styles.css') as css:
    st.markdown(f'<style>{css.read()}</style>', unsafe_allow_html=True)
subheaders = {
    "GPT-3 Completions": "GPT-3 Completions text-davinci-003 Engine",
    "GPT-3 Classification": "a",
    "GPT-3 Summarization": "b",
    "GPT-3 Image Generation": "Image Generation Model",
    "Keras Example 1": "d",
    "Keras Example 2": "e",
    "Pandas Dataframe": "f",
}
if not ("page" in st.session_state):
    st.title("Application for AI")
    st.subheader('Different Applications using AI tools and libraries')


def showheaders():
    st.title(st.session_state.page)
    st.subheader(subheaders[st.session_state.page])


sidebar.show()


if st.session_state.page == "GPT-3 Completions":
    showheaders()
    gpt3.completions()
if st.session_state.page == "GPT-3 Classification":
    showheaders()
    gpt3.classification()
if st.session_state.page == "GPT-3 Summarization":
    showheaders()
    gpt3.summarization()
if st.session_state.page == "GPT-3 Image Generation":
    showheaders()
    gpt3.image()
