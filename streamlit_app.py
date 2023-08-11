import streamlit as st
from langchain.llms import OpenAI

st.title('🦜🔗 Job Search help App')

st.info("Please use the side bar Menu to choose what you would like to do ..., After entering the Open API Key.")
st.info("LINK to source code: https://github.com/pramodkoshy/streamlit-jobhelp.git")

if "openai_api_key" not in st.session_state:
    st.session_state["openai_api_key"] = ""


# the below functions are to keep a copy of the state which gets erazed when the text widget gets cleaned up during a page change

def keep(key):
    # Copy from temporary widget key to permanent key
    st.session_state[key] = st.session_state['_'+key]

def unkeep(key):
    # Copy from permanent key to temporary widget key
    st.session_state['_'+key] = st.session_state[key]


unkeep("openai_api_key")
st.sidebar.text_input("OpenAI API Key", key="_openai_api_key", on_change=keep, args=["openai_api_key"])




def generate_response(input_text):   
  llm = OpenAI(temperature=0.7, openai_api_key = st.session_state["openai_api_key"])
  return llm(input_text)

