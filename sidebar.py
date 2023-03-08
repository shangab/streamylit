import streamlit as st

def show():
    with st.sidebar:
        st.image("./assets/img/abu2.jpeg", width=120)
        st.subheader('By: Abubaker Shangab')
        st.session_state.nlp= st.radio("Natural Language Processing",("Huggingface Transformrs","NLP Operations", "Openai API Models"))
        st.session_state.ml=st.radio("Machine Learning",("Tensorflow Keras","Pytorch"))
        st.session_state.bi=st.radio("Business Intelligence",("Pandas Dashboard","BI Basics"))
        
        if st.session_state.nlp=='Openai API Models':
            st.session_state.nlp= st.radio("Openai API Models",("GPT-3 Completions","GPT-3 Classification", "GPT-3 Summarization"))

        