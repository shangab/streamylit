import streamlit as st


def show():
    st.title(":house: Home")
    st.subheader(
        "This page implements different topics in data science,AI, NLP and OpenAI GPT")
    st.subheader(
        "Find the code in [HF GIT](https://huggingface.co/spaces/shangab/shangapp/tree/main)")
    st.markdown("---")

    c1, c2 = st.columns([1, 9])
    c1.image("./assets/img/abu.png", width=100)
    c2.write(
        "Abubaker Hamid, is the creator of [Dalinga](https://dalinga.flowbytes.com/) Formal Senthetic Functional Language and [Flowbytes](https://www.flowbytes.com/) Platform writer. M.Sc in Artifiicial Intelligence from [SUST University](https://www.sustech.edu/), Sudan. M.Sc in Discrete Events Systems from [McMaster University](https://www.mcmaster.ca/), Canada. 23 years Experience in Software Engineering.")
    st.write("""
    Welcome to our website dedicated to showcasing different implementations of AI algorithms and BI tools using Python Streamlit!

Text is an integral part of our lives, and it plays a critical role in many applications of AI and BI. From natural language processing to sentiment analysis and text classification, text data is becoming increasingly important in our digital world. At our website, we offer a range of tools and algorithms that can help you work with text data and extract valuable insights.

One of the most popular applications of text data is natural language processing (NLP). NLP is a field of AI that deals with the interaction between humans and computers using natural language. It involves a range of techniques, including text analysis, language translation, and speech recognition. At our website, we offer a range of NLP tools that can help you analyze text data and extract valuable insights.

For example, our website provides implementations of algorithms like GPT-3, a cutting-edge language model that can generate human-like text. GPT-3 can be used for a range of applications, including chatbots, content generation, and language translation. We also offer a range of other NLP tools like sentiment analysis algorithms that can help you analyze the sentiment of text data, and text classification algorithms that can help you classify text data into different categories.

In addition to NLP, our website also offers a range of BI tools that can help you visualize and analyze text data. Our tools are designed to be user-friendly and accessible to both data scientists and non-technical users. For example, we offer tools like word clouds and topic modeling that can help you visualize the most common words or topics in your text data. We also offer more advanced tools like network analysis that can help you analyze the relationships between different words or topics in your data.

At our website, we strive to provide you with the latest and most innovative tools for working with text data. We are constantly updating our offerings and incorporating new algorithms and techniques as they become available. Whether you are a data scientist, a business analyst, or a student, our website has something to offer you. So why not check us out today and see how we can help you unlock the power of text data using Python Streamlit and AI algorithms and BI tools!
    
    """)
