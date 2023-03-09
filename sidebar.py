import streamlit as st
from streamlit_option_menu import option_menu


def show():
    with st.sidebar:
        st.image("./assets/img/abu2.jpeg", width=120)
        st.subheader('By: Abubaker Shangab')
        st.session_state.page = option_menu("App Menu",
                                            options=["Huggingface Transformrs",
                                                     "GPT-3 Completions",
                                                     "GPT-3 Classification",
                                                     "GPT-3 Summarization",
                                                     "GPT-3 Image Generation",
                                                     "Keras Example 1",
                                                     "Keras Example 2",
                                                     "Pandas Dataframe",
                                                     ],
                                            icons=[
                                                "emoji-smile-fill",
                                                "chat-dots",
                                                "layout-split",
                                                "arrows-collapse",
                                                "chat-dots",
                                                "chat-dots",
                                            ], menu_icon="cast")
