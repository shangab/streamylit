import streamlit as st
import sidebar
import gpt3

with open('assets/css/styles.css') as css:
    st.markdown(f'<style>{css.read()}</style>',unsafe_allow_html=True)

st.title('NLP, GPT-3 and Machine Learning')
st.subheader('Different Applications using AI tools and libraries')

st.session_state.nlp=''
st.session_state.ml=''
st.session_state.bi=''


sidebar.show()

if st.session_state.nlp=="GPT-3 Completions":
    gpt3.completions()

if st.session_state.nlp=="GPT-3 Classification":
    gpt3.classification()
if st.session_state.nlp=="GPT-3 Summarization":
    gpt3.summarization()
