import os
from dotenv import load_dotenv,dotenv_values

from langchain_community.llms import Ollama 

import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langsmith import traceable


load_dotenv() #We will load all the env variables
#Once we ran this, we do not need to run os.getenv() again, because we have already loaded the keys to the current process memory

#langsmith tracking 
values = dotenv_values(".env")  # returns a dict of key→value from that file, we check whether we have loaded the keys or not
print(values.keys()) #with this we can confirm, we have loaded the openai api key

## Prompt Template
prompt = ChatPromptTemplate.from_messages(
    {
        ('system','You are a helpful assistant, Please respond to the question asked '),
        ("user","Question: {question}")
    }
)

#Streamlit framework
st.title("Langchain demo with Qwen3")
input_text = st.text_input("Hello there, what do you want?")

##Ollama model
llm = Ollama(model='qwen3:4b')

#set output parser
output_parser = StrOutputParser()

#create a chain with input --> model --> output
chain = prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({"question": input_text}))
