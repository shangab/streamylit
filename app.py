import streamlit as st
import ModSidebar
import ModOpenAI
import ModMissi
import ModBI
import ModHuggingface
import ModHome
import ModUtils as ut

st.set_page_config(layout="wide")

with open('assets/css/styles.css') as css:
    st.markdown(f'<style>{css.read()}</style>', unsafe_allow_html=True)


ModSidebar.show()

if st.session_state.page == "🏠 Home":
    ModHome.show()

if st.session_state.page == "🤗 HF Transformrs":
    ModHuggingface.show()

if st.session_state.page == "🧠 GPT-3 Completions":
    ModOpenAI.completions()

if st.session_state.page == "🧠 GPT-3 Classification":
    ModOpenAI.classification()

if st.session_state.page == "🧠 GPT-3 Summarization":
    ModOpenAI.summarization()

if st.session_state.page == "🧠 GPT-3 Image Generation":
    ModOpenAI.image()

if st.session_state.page == "💹 BI Sales Dashboard":
    st.title(":chart: BI Sales Dashboard")
    st.subheader(
        "DOC: supermarket_sales - Sheet1.csv from [kaggle](https://www.kaggle.com/code/agnithc/supermarket-sales-analysis)")
    st.subheader(
        ":arrow_lower_left::arrow_lower_left: Filter Criteria in Sidebar :arrow_lower_left: :arrow_lower_left: ")
    st.write('In this example we used :panda_face: pandas and :bar_chart: plotly python libraries as well as streamlit framework.\n We did the data munging. We also used streamlit caching to enhance processing. ')
    st.markdown("---")
    with st.expander("View Code", expanded=False):
        st.code(ut.getSource(ModBI.sales))
    ModBI.sales()

if st.session_state.page == "🤗 RoBERTa fill<mask>":
    ModMissi.fillMask()
