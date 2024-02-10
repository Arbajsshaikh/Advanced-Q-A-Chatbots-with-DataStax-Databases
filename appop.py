from langchain.llms import OpenAI


import streamlit
import os
import streamlit as st

OPENAI_API_KEY="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"

def get_response(x):
    llm=OpenAI(openai_api_key=os.environ['OPENAI_API_KEY'])
    y=llm(x)
    return y

st.set_page_config(page_title="Q&A Demo")

st.header("langchain integrating OpenAI chatbot")

input=st.text_input("Input:  ",key='input')

response=get_response(input)

submit=st.button('ask anything')

if submit:
    st.subheader('AI Response')
    st.write(response)