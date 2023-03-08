import streamlit as st
import openai
from streamlit_chat import message
import sidebar

openai.api_key = st.secrets["OPENAI_API_SECRET"]

st.title('NLP, GPT-3 and Machine Learning')
st.header('Application using AI python tools and libraries')
st.subheader('By: Abubaker Shangab')
sidebar.show()


def get_completions(prompt):
    completions = openai.Completion.create(
        engine='text-davinci-003', max_tokens=100, prompt=prompt)
    return completions.choices


if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'prompts' not in st.session_state:
    st.session_state['prompts'] = []

def get_prompt():
    prompt= st.text_input("You:", "Hello how are you?",key="input")
    return prompt

prompt = get_prompt()

if prompt:
    results = get_completions(prompt)
    st.session_state.prompts.append(prompt)
    st.session_state.generated.append(results[0].text)
    prompt=''

if st.session_state['generated']:
    for i in range(len(st.session_state['generated'])-1, -1, -1):
        g1,g2,g3=st.columns([1,7,2])
        u1,u2,u3=st.columns([2,7,1])
        g1.write(':face:')
        g2.write(st.session_state["generated"][i])
        u2.write(st.session_state['prompts'][i])
        u3.write(':face:')
        
        # message(st.session_state["generated"][i], key=str(i))
        # message(st.session_state['prompts'][i], is_user=True, key=str(i) + '_user')