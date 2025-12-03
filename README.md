
# 🚀 **Generative-AI — My Journey Into LLMs, RAG, and LangChain**

## 🧠 **Overview**

This repository documents my hands-on learning journey in **Generative AI**, covering core concepts like **LLMs, RAG pipelines, LCEL (LangChain Expression Language), message history**, and building **Streamlit-based interfaces** for large language models.
It includes experiments, notebooks, and implementations that helped me understand how modern AI systems are built end-to-end.

---

# 📘 **What This Repository Contains**

### **1️⃣ Getting Started with LLMs**

* Basics of prompting and interacting with LLMs
* Understanding ChatModels vs LLMs
* First notebook exploring LangChain primitives

### **2️⃣ Building LLM Applications**

* Created a **Streamlit interface** for generating responses
* Integrated an LLM into a minimal app flow
* Explored input/output parsing

### **3️⃣ LCEL (LangChain Expression Language)**

* Learned LCEL syntax
* Built a simple pipeline using chains
* Applied structured output + message templates
* Developed a small LCEL-based application

### **4️⃣ Message History & Sessions**

* Used **RunnableWithMessageHistory**
* Explored session-based memory
* Implemented chat history storage
* Understood how RAG applications maintain state

### **5️⃣ Recursive Text Splitting & Data Transformation**

* Used **RecursiveCharacterTextSplitter**
* Cleaned, chunked, and prepared text for vectorization
* Processed files like `speech.txt` for use in RAG pipelines

### **6️⃣ Document Loaders**

* Loaded text files using LangChain loaders
* Understood how loaders integrate with vector databases

### **7️⃣ Implementing the Full RAG Chain**

* Built a complete Retrieval Augmented Generation flow
* Text splitting → embeddings → retriever → LLM response
* Implemented inside `Message_History.ipynb`
* Integrated memory + RAG for more contextual answers

---

# 🧩 **Folder Structure**

```
Generative-AI/
│── 2)Building/
│── 3)LCEL_ipynb/
│── 4)Message_History.ipynb
│── Getting_Started.ipynb
│── speech.txt
│── requirements.txt
│── RIA_Resume.pdf
│── .gitignore
│── README.md
```

---

# 🛠️ **Technologies & Tools**

* **LangChain**
* **OpenAI / LLM APIs**
* **Streamlit**
* **Python**
* **Embeddings & Text Splitters**
* **Chains, Runnables, Memory**
* **Jupyter Notebooks**

---

# 🏗️ **Key Concepts Learned**

### ✔️ Prompt Engineering

### ✔️ ChatModels vs LLMs

### ✔️ LCEL chaining

### ✔️ Message history + sessions

### ✔️ Retrieval Augmented Generation (RAG)

### ✔️ Text splitting & vectorization

### ✔️ Streamlit LLM apps

### ✔️ Loading & transforming documents

---

# 🚀 **Future Additions**

* Add vector DB integration (FAISS / Chroma)
* Expand RAG system into a full-fledged chatbot
* Integrate tools / agents
* Convert notebooks into a production-ready project

---

# 👩‍💻 **Author**

**Ria Pandey**
AI | ML | GenAI Enthusiast
📍 VIT Bhopal
