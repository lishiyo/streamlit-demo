import streamlit as st
from langchain.llms import OpenAI

st.title('🦜🔗 Quickstart App')

openai_api_key = st.sidebar.text_input('OpenAI API Key')

def generate_response(input_text, temperature=0.7, max_tokens=-1, top_p=1.0, frequency_penalty=0.0, presence_penalty=0.0, stop=['\n']):
  # https://api.python.langchain.com/en/latest/llms/langchain.llms.openai.OpenAI.html
  llm = OpenAI(temperature, openai_api_key=openai_api_key)
  st.info(llm(input_text))

with st.form('my_form'):
  text = st.text_area('Enter text:', 'What are the three key pieces of advice for learning how to code?')
  submitted = st.form_submit_button('Submit')
  if not openai_api_key.startswith('sk-'):
    st.warning('Please enter your OpenAI API key!', icon='⚠')
  if submitted and openai_api_key.startswith('sk-'):
    generate_response(text)