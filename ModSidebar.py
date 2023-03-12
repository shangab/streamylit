import streamlit as st
from streamlit_option_menu import option_menu


def expandMainMenu():
    if 'page' not in st.session_state:
        return True
    if 'page' in st.session_state and not st.session_state.page == '💹 BI Sales Dashboard':
        return True
    return False


def show():
    with st.sidebar:
        st.image("assets/img/abu.png", width=150)
        st.subheader('Abubaker Shangab')
        st.session_state.page = option_menu(
            None,
            menu_icon="cast",
            options=["🏠 Home",
                     "🤗 HF Transformrs",
                     "🧠 GPT-3 Completions",
                     "🧠 GPT-3 Classification",
                     "🧠 GPT-3 Summarization",
                     "🧠 GPT-3 Image Generation",
                     "💹 BI Sales Dashboard",
                     "🤗 RoBERTa fill<mask>",
                     ],
            icons=[
                "house",
                "emoji-smile-fill",
                "chat-dots",
                "layout-split",
                "arrows-collapse",
                "image",
                "bar-chart-fill",
                "mask",
            ],
            default_index=0
        )
