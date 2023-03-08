import streamlit as st
import openai
from streamlit_chat import message

openai.api_key = st.secrets["OPENAI_API_SECRET"]


def get_completions(prompt):
    completions = openai.Completion.create(
        engine='text-davinci-003', max_tokens=100, prompt=prompt)
    return completions.choices


st.title('Playing with NLP and GPT-3')
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
        message(st.session_state["generated"][i], key=str(i))
        message(st.session_state['prompts'][i], is_user=True, key=str(i) + '_user')