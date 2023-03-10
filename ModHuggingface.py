import streamlit as st
from transformers import pipeline
import plotly.express as px
import pandas as pd
import ModUtils as ut


def show():
    st.title("🤗 Huggingface Transformrs")
    st.subheader(
        "Find more about [Huggingface Transformers](https://huggingface.co/docs/transformers/index)")
    st.write('In the following examples we used  🤗 Huggingface Transformrs pretrained NLP models to accomplish the following tasks.')
    st.write('Use the Previous and Next buttons to see the examples.')
    b1, lbl, b2 = st.columns([1, 8, 1])
    if "hf" not in st.session_state:
        st.session_state.hf = 0
    if b1.button("Previous"):
        if st.session_state.hf > 0:
            st.session_state.hf -= 1
    if b2.button("Next"):
        if st.session_state.hf < 3:
            st.session_state.hf += 1

    st.markdown("---")

    def sentimentAnayze(text):
        with st.spinner("Please wait"):
            classifier = pipeline("sentiment-analysis")
            result = classifier(text)
            return result

    if st.session_state.hf == 0:
        st.header('Sentiment Analysis')

        st.code(ut.getSource(sentimentAnayze), language="python")
        prompt = st.text_input('A text to classify (POSITIVE or NEGATIVE):')
        ans = st.empty()
        if st.button("Classify Sentence") and prompt:
            result = sentimentAnayze(prompt)
            c1, c2 = st.columns(2)
            c1.write(result)
            scores = [0, 0]
            if result[0]['label'] == 'POSITIVE':
                scores = [10, 0]
            else:
                scores = [0, 10]
            data = pd.DataFrame(
                {'mode': ['POSITIVE', 'NEGATIVE'], 'score': scores})
            chart = px.bar(
                data, x='mode', y='score',
                width=250, height=200
            )
            c2.plotly_chart(chart)

    def zeroShotClassification(prompt, topic_list):
        with st.spinner("Please waint..."):
            classifier = pipeline("zero-shot-classification")
            labels = topic_list.split(",")
            result = classifier(prompt, candidate_labels=labels)
            return result

    if st.session_state.hf == 1:
        st.header('Zero-Shot-Classification')
        st.write(
            "Using the zero-shot-classification to classify text on givern comma separated topics")
        st.code(ut.getSource(zeroShotClassification))
        prompt = st.text_input('A prompt to classify',
                               value="Last year I spend a lot of time focussing on Math and Science")
        topic_list = st.text_input('A comma separated topics to closify the text on',
                                   value="Academic,Politics,Art,Sport")

        ans = st.empty()
        if st.button("Classify Text") and prompt:
            result = zeroShotClassification(prompt, topic_list)
            ans.write(result)
            data = pd.DataFrame({'Topics': result['labels'], 'Scores': [
                                round(x*100, 0) for x in result['scores']]})
            chart = px.bar(data, x='Topics', y='Scores',
                           title='<b>Scores multiplied by 100 and integerized</b>')
            st.plotly_chart(chart)

    def textGenerate(prompt):
        with st.spinner("Please waint..."):
            genertor = pipeline("text-generation", model="distilgpt2")
            text = genertor(prompt)
            return text
    if st.session_state.hf == 2:
        st.header('Text Generation')
        st.write('Using the distilgpt2 on text-generaiton task.')
        st.code(ut.getSource(textGenerate))
        prompt = st.text_input('A prompt to guide the model :',
                               value="In this course we will teach you how to")
        ans = st.empty()
        if st.button("Generate Text") and prompt:
            result = textGenerate(prompt)
            ans.write(result)

    def summarize(article,  model_name="t5-base"):
        with st.spinner("Please waint..."):
            summarizer = pipeline("summarization", model=model_name,
                                  tokenizer="t5-base", framework="tf")
            return summarizer(article)
    if st.session_state.hf == 3:
        st.header('Transformers Summarization')
        st.write("We are using this model: facebook/bart-large-cnn, however you can use other trained models from huggingface transformers.")
        st.code(ut.getSource(summarize), language="python")

        prompt = st.text_area('A text to summarize please:', value="""
        Academic article
            Information overload occurs when decision-makers face a level of information that is greater than their information processing capacity, i.e., an overly high information load (Schroder et al. 1967; Eppler and Mengis 2004), but the phenomenon is not confined to the modern world. As Blair (2012) noted in her review article, even in the thirteenth century, scholars complained of “the key ingredients of the feeling of overload which are still with us today: ‘the multitude of books, the shortness of time and the slipperiness of memory’” (Blair 2012, p. 1).

            Two radical innovations supported the rapid increase in the availability of information and the decrease in information search-related costs: Gutenberg’s printing innovations and the rise of information technology (IT). Before these radical innovations, the issue of information overload was limited to a wealthy and privileged elite. In particular, the rise of IT and the use of internet services have resulted in an expansion of information overload-related problems for all social ranks. In ancient and medieval times, the nobility and academics almost exclusively faced information overload-related problems, as Blair (2012) and Levitin (2014) suggested.
        """)
        model = st.text_input("Model to use", value="t5-base")
        ans = st.empty()
        if st.button("Summarize Article") and prompt:
            summary = summarize(prompt, model)
            ans.write(summary)
