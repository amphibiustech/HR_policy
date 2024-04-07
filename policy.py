import streamlit as st 
from langchain_community.vectorstores import FAISS 
import google.generativeai as genai 
import os 
import io
import warnings
warnings.filterwarnings('ignore')
import logging
logging.basicConfig(level=logging.WARN,
                    filename="logs.log",
                    filemode="a",
                    format="%(asctime)s - %(levelname)s - %(message)s",
                    datefmt="%Y-%m-%d %H:%M:%S")
from dotenv import load_dotenv
from sqlalchemy import create_engine
from langchain_community.embeddings import HuggingFaceEmbeddings
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_core.prompts import ChatMessagePromptTemplate,ChatPromptTemplate,PromptTemplate
from langchain_google_genai import GoogleGenerativeAIEmbeddings,ChatGoogleGenerativeAI
from langchain.chains.question_answering import load_qa_chain


def uploaded_pdf(pdf):
    text = ""
    with io.BytesIO(pdf.read()) as file:
        reader = PdfReader()
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            text += page.extract_text()
    return text

def get_text_splitter(document):
    splitter = RecursiveCharacterTextSplitter(chunk_size=5000,chunk_overlap=500)
    return  splitter.split_documents(document)

def get_vector_embed(chunks):
    embed = genai.em




def main():
    st.set_page_config(page_title="HR Policy | Amphibius",layout="centered",
                       page_icon=":robot:",
                       initial_sidebar_state="expanded",)
    
    st.header("Ask a Question to your GenAI enabled ChatBot for HR related policies ! :male-technologist:")
    email = st.text_input("Enter you email id :")
    question = st.text_input("Ask a question on HR Policy :")
    if st.button("Submit"):
        with st.spinner("Processing"):
            if email.strip() == "" or question.strip() == "":
                if email.strip() == "":
                    st.warning("Email field is blank. Please fill in your email ID.")
                if question.strip() == "":
                    st.warning("Question field is blank. Please ask a question about HR policy.")
            else:
                st.write(f"Email ID is : {email}")
                st.write(f"Question is : {question}")

            
    
    with st.sidebar:
        st.subheader("This chatbot is powered by :")
        st.markdown("- :blue[Streamlit]")
        st.markdown("- :blue[Langchain]")
        st.markdown("- :blue[LLM]")
        st.markdown("- :blue[SQL]")
        st.text("")
        st.text("")
        st.text("") 
        st.text("") 
        st.text("") 
        st.text("") 
        st.text("") 
        
        
        
        st.markdown("---")
        st.markdown("""This application is developed by **@AmphibiusTech** [2024-25]. 
                    For more information, write us amphibiustech@gmail.com""")

        
      
if __name__ == "__main__":
    main()