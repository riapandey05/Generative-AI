# we will deploy langchain runnables and chains as rest api
# with the help of langserve we will be able to create rest api endpoints
from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
# from langchain_groq import StrOutputParser
from langchain_groq import ChatGroq
from langserve import add_routes
import os
from dotenv import load_dotenv
load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")
llm = ChatGroq(model="groq/compound",groq_api_key=groq_api_key)
# chatgroq is a wrapper around groq which is used to interact with groq

# 1. create a prompt template
system_template = "Translate the follwing into {language}:"
prompt_template = ChatPromptTemplate.from_messages([
    ("system", system_template),
    ("user", "{text}")
])

# 2. create output parser
parser = StrOutputParser()

# 3 create chain
chain = prompt_template | llm | parser

# 4. app definition
app = FastAPI(title="Lanchain Server",version="1.0",description="Langchain with Groq and FastAPI")
add_routes(app,chain,path="/chain")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app,host="127.0.0.1",port=8000)
