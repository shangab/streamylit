import streamlit as st
import sidebar
import gpt3
import ml

with open('assets/css/styles.css') as css:
    st.markdown(f'<style>{css.read()}</style>',unsafe_allow_html=True)

st.title('NLP, GPT-3 and Machine Learning')
st.subheader('Different Applications using AI tools and libraries')

st.session_state.page=''

sidebar.show()


if st.session_state.nlp=="GPT-3 Completions":
    gpt3.completions()

if st.session_state.nlp=="GPT-3 Classification":
    st.session_state.ml=''
    gpt3.classification()
if st.session_state.nlp=="GPT-3 Summarization":
    st.session_state.ml=''
    gpt3.summarization()

if st.session_state.ml=='Example 1':
    st.session_state.nlp=''
    ml.kerasExample1()
if st.session_state.ml=='Example 2':
    st.session_state.nlp=''
    ml.kerasExample2()