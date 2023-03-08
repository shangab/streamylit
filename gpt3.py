import streamlit as st
import openai
import json
import sys

API_KEY = st.secrets["OPENAI_API_SECRET"]
openai.api_key=API_KEY

def completions():
    def get_completions(prompt):
        stream=False
        try:
            # st.session_state.answ=''
            request = openai.Completion.create(
                engine='text-davinci-003', max_tokens=100, prompt=prompt, stream=stream)
            st.session_state.generated.append(request.choices[0].text)
            
            # for resp in request:
            #     sys.stdout.write(resp.choices[0].text)
            #     st.session_state.answ+=resp.choices[0].text
            #     st.session_state.generated[len(st.session_state.generated)-1]+=resp.choices[0].text
            #     sys.stdout.flush()
        except:
            e = sys.exc_info()[0]
            st.error(e)

    if 'generated' not in st.session_state:
        st.session_state['generated'] = []

    if 'prompts' not in st.session_state:
        st.session_state['prompts'] = []

    def get_prompt():
        c1,c2,c3=st.columns([1,7,2])
        c1.markdown(':man_in_tuxedo:')
        if c3.button("Clear"):
            st.session_state['prompts'] = []
            st.session_state['generated'] = []
        return c2.text_input("What is in your mind?",key="input")

    prompt = get_prompt()

    if prompt:
        get_completions(prompt)
        st.session_state.prompts.append(prompt)

    if st.session_state['generated']:
        for i in range(len(st.session_state['generated'])-1, -1, -1):
            g1,g2,g3=st.columns([1,7,2])
            u1,u2,u3=st.columns([2,7,1])
            g1.markdown(':brain:')
            g2.write(st.session_state["generated"][i])
            u2.write(st.session_state['prompts'][i])
            u3.markdown(':man_in_tuxedo:')

def classification():
    st.write('Stay tuned classification coming soon ...')

def summarization():
    st.write('Stay tuned summarization coming soon ...')