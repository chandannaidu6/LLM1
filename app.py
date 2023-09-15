import streamlit as st
from langchain.llms import OpenAI

st.title('Quickstart App')
openai_api_key = st.sidebar.text_input('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')

def generate_response(input_text):
    llm=OpenAI(temperature=0.7,openai_api_key=openai_api_key)
    st.info(llm(input_text))

with st.form('my_form'):
    text=st.text_area('Enter text:','What are the three key peices of advice for coding?')
    submitted = st.form_submit_button('Submit')
    if not openai_api_key.startswith('sk-'):
        st.warning('Please enter your openapi key',icon='⚠')
    if submitted and openai_api_key.startswith('sk-'):
        generate_response(text)