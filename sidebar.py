import streamlit as st
from streamlit_option_menu import option_menu


def show():
    with st.sidebar:
        st.image("./assets/img/abu2.jpeg", width=120)
        st.subheader('By: Abubaker Shangab')
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
                     ],
            icons=[
                "emoji-smile-fill",
                "chat-dots",
                "layout-split",
                "arrows-collapse",
                "chat-dots",
                "bar-chart-fill",
            ],
            default_index=0

        )
