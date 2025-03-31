import os
from dotenv import load_dotenv
from langchain.llms import Ollama  

# Configure the LLM - using Ollama
llm = Ollama(
    model="llama3",  
    temperature=0.7
)