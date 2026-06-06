#integrate my code with gemini API
import os
from constants import gemini_key
from langchain_google_genai import ChatGoogleGenerativeAI
import streamlit as st
from langchain_core.prompts import PromptTemplate
# from langchain.chains import LLMChain
from langchain_core.output_parsers import StrOutputParser


## streamline framework
os.environ["GOOGLE_API_KEY"] = gemini_key

st.title("celebrity search")
input_text = st.text_input("search the topic u want")

# prompt template
first_template = PromptTemplate(
    input_variables=["name"],
    template="What is {name}?"
)

second_template = PromptTemplate(
    input_variables=["person"],
    template="when was {person} born?"
)

##gemini llm 
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.8,
    max_tokens=2048 
)

chain1 = first_template | llm | StrOutputParser()
chain2 = second_template | llm | StrOutputParser()


if input_text:
    person_info = chain1.invoke({"name": input_text})
    born_info = chain2.invoke({"person": input_text})

    st.subheader("About the Celebrity")
    st.write(person_info)

    st.subheader("Birth Details")
    st.write(born_info)


