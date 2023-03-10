import streamlit as st
import openai
import ModUtils as ut

API_KEY = st.secrets["OPENAI_API_SECRET"]
openai.api_key = API_KEY


def completionsFunc(prompt, answer_area, error_area):
    with st.spinner("Please wait"):
        block = ''
        try:
            request = openai.Completion.create(
                engine='text-davinci-003', max_tokens=1000, prompt=prompt, stream=True)
            for resp in request:
                block += resp.choices[0].text
                answer_area.write(block)
        except:
            error_area.error('Error happened')


def completions():
    st.title(":brain: GPT-3 Completions")
    st.subheader("GPT-3 Completions text-davinci-003 Engine")
    st.write(
        'GPT (Generative Pre-trained Transformer) is a type of language model developed by OpenAI that is trained on a large corpus of text using unsupervised learning techniques. One of the key features of GPT is its ability to generate coherent and meaningful text based on a given prompt or input. Here I am using streamlit library to call the [OpenAI API](https://openai.com/blog/openai-api)')
    st.write('OpenAI API is a language processing service that provides access to state-of-the-art machine learning models for natural language tasks.')
    st.write('Try the model below ')
    st.markdown("---")

    st.code(ut.getSource(completionsFunc))

    prompt = st.text_input('AI: What is up?')
    ans = st.empty()
    err = st.empty()

    if prompt:
        completionsFunc(prompt, ans, err)


def imageFunc(prompt, answer_area):
    with st.spinner("Please wait"):
        res = openai.Image.create(
            prompt=prompt,
            n=2,
            size="1024x1024")
    for one in res.data:
        answer_area.markdown(f'[image]({one.url})', unsafe_allow_html=True)
        st.image(one.url)


def image():
    st.title(":brain: GPT-3 Image Genration")
    st.subheader(
        "GPT-3 Image Generation using GAN (Generative Adversarial Networks)")
    st.write("OpenAI uses a combination of deep learning algorithms, primarily generative adversarial networks (GANs), to generate images. GANs consist of two neural networks: a generator network and a discriminator network. The generator network takes random noise as input and generates images, while the discriminator network tries to distinguish between real images and generated images. The two networks are trained together in an adversarial process, where the generator tries to fool the discriminator, and the discriminator tries to correctly identify real images. As the training progresses, the generator learns to generate more realistic images that can fool the discriminator.")
    st.markdown("---")
    st.code(ut.getSource(imageFunc))
    prompt = st.text_input('Describe the image')
    ans = st.empty()

    if st.button("Generate Images!") and prompt:
        imageFunc(prompt, ans)


def classificationFunc(prompt, labels, answer_area, error_area):
    with st.spinner("Please wait"):
        try:
            request = openai.Classification.create(
                model='text-davinci-002',
                query=prompt,
                labels=labels,
            )
            if request.label:
                predicted_label = request.label
                answer_area.write(predicted_label)
            else:
                error_area("Error:", request)
        except:
            error_area.error('Error happened')


def classification():
    st.title(":brain: GPT-3 Classification")
    st.subheader(
        "GPT-3  Classification")
    st.write("GPT-3's classification engine is a neural network that uses deep learning techniques to perform text classification. It is pre-trained on a large corpus of text and fine-tuned on specific classification tasks, such as sentiment analysis or topic classification. The model can predict the probability of a given text belonging to a particular category or class, and it can be further improved with additional training data.")
    st.markdown("---")
    st.code(ut.getSource(classificationFunc))
    prompt = st.text_area(
        'A text to classify from the belwo topics: (Buggy, will fix soon)')
    labels = ["Academic", "Politics", "Religious"]
    st.json(labels)
    ans = st.empty()
    err = st.empty()

    if st.button("Classify Article") and prompt:
        classificationFunc(prompt, labels, ans, err)


def summarizationFunc(prompt, answer_area, error_area):
    with st.spinner("Please wait..."):
        try:
            request = openai.Completion.create(
                engine='davinci', max_tokens=60, prompt=prompt,
                n=1,
                stop=None,
                temperature=0.5,
                stream=False
            )
            if request.choices[0].text:
                summarized_text = request.choices[0].text.strip()
                answer_area.write(summarized_text)
            else:
                error_area.write("Error Happened")
        except:
            error_area.error('Error happened')


def summarization():
    st.title(":brain: GPT-3 Summarization")
    st.subheader(
        "GPT-3 Summarization")
    st.write(
        'GPT (Generative Pre-trained Transformer) is a type of language model developed by OpenAI that is trained on a large corpus of text using unsupervised learning techniques. One of the key features of GPT is its ability to generate coherent and meaningful text based on a given prompt or input. Here I am using streamlit library to call the [OpenAI API](https://openai.com/blog/openai-api)')
    st.write('OpenAI API is a language processing service that provides access to state-of-the-art machine learning models for natural language tasks.')
    st.write('Try the model below ')
    st.markdown("---")
    st.code(ut.getSource(summarizationFunc))
    prompt = st.text_area('A text to summarize please:')
    ans = st.empty()
    err = st.empty()

    if st.button("Summarize Article") and prompt:
        summarizationFunc(prompt, ans, err)
