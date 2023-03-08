import streamlit as st

def show():
    with st.sidebar:
        st.checkbox("Home")
        st.checkbox("NLP Operations")
        st.checkbox("Huggingface Transformrs")
        st.checkbox("Tensorflow Keras")
        st.checkbox("Pytourch")
    
    