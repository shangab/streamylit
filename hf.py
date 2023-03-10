import streamlit as st


def show():
    st.title("🤗 Huggingface Transformrs")
    st.subheader(
        "Find more about [Huggingface Transformers](https://huggingface.co/docs/transformers/index)")
    st.subheader("They are the base of ChatGPT")
    st.write('In this example we used :panda_face: pandas and :bar_chart: plotly python libraries as well as streamlit framework.\n We did the data munging. We also used streamlit caching to enhance processing. ')
    st.markdown("---")
    if st.checkbox('See what they say about their Transformers:'):
        st.write("""
    State-of-the-art Machine Learning for PyTorch, TensorFlow, and JAX.

🤗 Transformers provides APIs and tools to easily download and train state-of-the-art pretrained models. Using pretrained models can reduce your compute costs, carbon footprint, and save you the time and resources required to train a model from scratch. These models support common tasks in different modalities, such as:

📝 Natural Language Processing: text classification, named entity recognition, question answering, language modeling, summarization, translation, multiple choice, and text generation.
🖼️ Computer Vision: image classification, object detection, and segmentation.
🗣️ Audio: automatic speech recognition and audio classification.
🐙 Multimodal: table question answering, optical character recognition, information extraction from scanned documents, video classification, and visual question answering.

🤗 Transformers support framework interoperability between PyTorch, TensorFlow, and JAX. This provides the flexibility to use a different framework at each stage of a model’s life; train a model in three lines of code in one framework, and load it for inference in another. Models can also be exported to a format like ONNX and TorchScript for deployment in production environments.
    
    
    """)


def show2():
    st.write("""
    Exciting news! Our website will soon be implementing Hugging Face Transformers, the state-of-the-art library for natural language processing and machine learning.

    Hugging Face Transformers is a powerful library that allows you to easily train and deploy state-of-the-art models for a variety of NLP tasks, such as sentiment analysis, text classification, and language translation. With its user-friendly interface and comprehensive documentation, Hugging Face Transformers is perfect for both beginners and experienced data scientists.

    By implementing Hugging Face Transformers, our website will be able to offer even more advanced and cutting-edge tools for working with text data. You can expect to see new algorithms and techniques added to our existing offerings, as well as increased performance and accuracy in our existing models.

    Whether you are a data scientist, a business analyst, or a student, the addition of Hugging Face Transformers to our website is sure to provide you with new and exciting opportunities to work with text data. So be sure to follow us in the coming days as we roll out these exciting new features and tools.
    """)
