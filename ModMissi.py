import streamlit as st
import requests
import ModUtils as ut

HF_API_KEY = st.secrets["HF_API_SECRET"]


def callFillMask(prompt):
    with st.spinner("Please wait..."):
        API_URL = "https://api-inference.huggingface.co/models/roberta-base"
        HF_HEADERS = {
            "Authorization": f"Bearer {HF_API_KEY}"
        }
        headers = HF_HEADERS
        payload = {
            "inputs": prompt,
        }
        response = requests.post(API_URL, headers=headers, json=payload)
        return response.json()


def fillMask():
    st.title(
        "🤗 Huggingface [RoBERTa-base](https://huggingface.co/roberta-base) Models")
    st.subheader(
        "This one is the [Fill-Mask Model](https://huggingface.co/tasks/fill-mask)")
    st.write(
        'In the following example we used  🤗 Huggingface Inference API for some cool NLP models.')
    st.write('Masked language modeling is the task of masking some of the words in a sentence and predicting which words should replace those masks. These models are useful when we want to get a statistical understanding of the language in which the model is trained in.')
    st.markdown("---")
    with st.expander("View Code"):
        st.code(ut.getSource(callFillMask))
    st.markdown("---")

    prompt = st.text_input('A sentence with a <mask>ed word',
                           value="Last year was <mask> to me."
                           )
    result = st.empty()
    if prompt and st.button("Unmask word"):
        output = callFillMask(prompt)
        result.write(output)
