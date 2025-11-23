# import os
# from dotenv import load_dotenv

# from langchain_community.llms import ollama
# import streamlit as st
# from langchain_core.prompts import ChatPromptTemplate
# from langchain_core.output_parsers import StrOutputParser
# load_dotenv()

# os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
# os.environ["LANGCHAIN_TRACING_V2"] = "true"
# os.environ["LANGCHAIN_PROJECT"]=os.getenv("LANGCHAIN_PROJECT")

# # streamlit framework
# st.title("Ollama with LangChain and Streamlit")
# input_text = st.text_input("What is in your mind...")

import os
from dotenv import load_dotenv

import streamlit as st
from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# ---------- ENV SETUP ----------
load_dotenv()

os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = os.getenv("LANGCHAIN_PROJECT")

# ---------- STREAMLIT PAGE CONFIG ----------
st.set_page_config(
    page_title="Ollama + LangChain Chat",
    page_icon="🤖",
    layout="wide",
)

st.title("🤖 Ollama with LangChain & Streamlit")
st.caption("Ask anything and get responses powered by a local Ollama model + LangChain.")

# ---------- SIDEBAR : SETTINGS ----------
with st.sidebar:
    st.header("⚙️ Settings")
    model_name = st.selectbox(
        "Ollama Model",
        ["gemma3:1b"],
        index=0,
        help="Choose the model you have pulled in Ollama.",
    )
    temperature = st.slider(
        "Creativity (temperature)",
        0.0,
        1.0,
        0.3,
        0.05,
        help="Higher = more creative, lower = more focused.",
    )

    st.markdown("---")
    if st.button("🧹 Clear conversation"):
        st.session_state.messages = []

# ---------- INIT SESSION STATE ----------
if "messages" not in st.session_state:
    st.session_state.messages = []

# ---------- LLM + CHAIN ----------
prompt = ChatPromptTemplate.from_template(
    """You are a helpful, friendly AI assistant.
Answer clearly and concisely in markdown.

User question: {question}
"""
)
output_parser = StrOutputParser()


def get_chain():
    llm = Ollama(model=model_name, temperature=temperature)
    return prompt | llm | output_parser


# ---------- CHAT HISTORY DISPLAY ----------
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ---------- USER INPUT ----------
user_input = st.chat_input("What is in your mind...")

if user_input:
    # show user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # get response
    chain = get_chain()
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = chain.invoke({"question": user_input})
            st.markdown(response)

    st.session_state.messages.append({"role": "assistant", "content": response})
