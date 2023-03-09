import streamlit as st
import openai

API_KEY = st.secrets["OPENAI_API_SECRET"]
openai.api_key = API_KEY


def completions():
    prom = st.text_input('What is up?')
    ans = st.empty()
    err = st.empty()

    def tryme(prom):
        with st.spinner("Please wait"):
            block = ''
            try:
                request = openai.Completion.create(
                    engine='text-davinci-003', max_tokens=100, prompt=prom, stream=True)
                for resp in request:
                    block += resp.choices[0].text
                    ans.write(block)
            except:
                err.error('Error happened')

    if prom:
        tryme(prom)


def image():
    prom = st.text_input('Describe the image')
    ans = st.empty()
    err = st.empty()

    def tryme(prom):
        with st.spinner("Please wait"):
            res = openai.Image.create(
                prompt=prom,
                n=2,
                size="1024x1024")
        for one in res.data:
            ans.markdown(f'[image]({one.url})', unsafe_allow_html=True)
            st.image(one.url)
    if prom:
        tryme(prom)


def classification():
    st.write('Stay tuned classification coming soon ...')


def summarization():
    st.write('Stay tuned summarization coming soon ...')
