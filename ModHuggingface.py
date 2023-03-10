import streamlit as st
import requests


def show():
    st.title("🤗 Huggingface Transformrs")
    st.subheader(
        "Find more about [Huggingface Transformers](https://huggingface.co/docs/transformers/index)")
    st.write('In this example we used :panda_face: pandas and :bar_chart: plotly python libraries as well as streamlit framework.\n We did the data munging. We also used streamlit caching to enhance processing. ')
    b1, lbl, b2 = st.columns([1, 8, 1])
    st.session_state.hf = 0
    if b1.button("Previous"):
        if st.session_state.hf > 0:
            st.session_state.hf -= 1
    if b2.button("Next"):
        if st.session_state.hf < 1:
            st.session_state.hf += 1

    st.markdown("---")

    def summarize(article):
        return "YEss"
    if st.session_state.hf == 0:
        st.header('Classification Labeling Model')
    if st.session_state.hf == 1:
        st.header('Transformers Summarization')
        st.code("""def summarize(article):
        return "YEss""", language="python")
