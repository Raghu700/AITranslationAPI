from src.config import GROQ_API_KEY
"""
This module sets up a FastAPI server to provide a translation service using the Langchain library and Groq model.
Modules:
    - src.config: Imports the GROQ_API_KEY for authentication.
    - langchain_groq: Provides the ChatGroq model for translation.
    - langchain_openai: Provides the ChatOpenAI model (not used in this code).
    - fastapi: FastAPI framework for building the API server.
    - langchain_core.output_parsers: Provides the StrOutputParser for parsing model output.
    - langchain_core.prompts: Provides the ChatPromptTemplate for creating prompt templates.
    - langserve: Utility to add routes to the FastAPI app.
    - uvicorn: ASGI server to run the FastAPI app.
Functions:
    - add_routes: Adds the translation chain route to the FastAPI app.
    - uvicorn.run: Runs the FastAPI app on the specified host and port.
Classes:
    - FastAPI: Main class for creating the FastAPI app.
    - ChatGroq: Class for creating the Groq model instance.
    - ChatPromptTemplate: Class for creating prompt templates.
    - StrOutputParser: Class for parsing the output of the model.
Variables:
    - model: Instance of the ChatGroq model with specified parameters.
    - system_template: Template string for the system message in the prompt.
    - prompt_template: Instance of ChatPromptTemplate created from the system and user messages.
    - parser: Instance of StrOutputParser for parsing the model output.
    - chain: The complete chain combining the prompt template, model, and parser.
    - app: Instance of the FastAPI app with specified title, version, and description.
"""
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from fastapi import FastAPI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langserve import add_routes
import uvicorn

# Create LLM model
model= ChatGroq(model="gemma2-9b-it", groq_api_key= GROQ_API_KEY)

#Create genric Template
from langchain_core.prompts import ChatPromptTemplate

system_template="translate the following into  {language}"
prompt_template= ChatPromptTemplate.from_messages(
    [
        ("system", system_template), 
        ("user","{text}")]
)

parser=StrOutputParser()

#Create chain
chain = prompt_template|model|parser

##App Definition
app=FastAPI(title="AI Agent langchain Server",
            version="1.0",
            description="A simple API server using Langchain runnable interfaces")

add_routes(
app,
chain,
path="/chain"

)
if __name__=="__main__":
    uvicorn.run(app, host="127.0.0.1",port=8000)