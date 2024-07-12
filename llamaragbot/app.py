import streamlit as st
from llama_index.llms.ollama import Ollama
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.embeddings.huggingface import HuggingFaceEmbedding

st.set_page_config(page_title="Chat with the Netscout document, powered by LlamaIndex", page_icon="🦙", layout="centered", initial_sidebar_state="auto", menu_items=None)

st.title("Chat with the Netscout data, powered by LlamaIndex 💬🦙")
st.info("Check out our website at [netscout.com](https://www.netscout.com/)", icon="📃")
         
if "messages" not in st.session_state.keys(): # Initialize the chat messages history
    st.session_state.messages = [
        {"role": "assistant", "content": "Ask me a question about Netscout!"}
    ]

@st.cache_resource(show_spinner=False)
def load_data():
    with st.spinner(text="Loading and indexing the Netscout docs – hang tight! This should take 1-2 minutes."):
        reader = SimpleDirectoryReader(input_dir="./netscout_data", recursive=True)
        docs = reader.load_data()
        llm = Ollama(model='llama3', request_timeout=300.0)
        embedding_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")
        index = VectorStoreIndex.from_documents(docs, embed_model=embedding_model)
        query_engine = index.as_query_engine(llm=llm)
        return query_engine

query_engine = load_data()

if "chat_engine" not in st.session_state.keys(): # Initialize the chat engine
        st.session_state.chat_engine = query_engine

if prompt := st.chat_input("Your question"): # Prompt for user input and save to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

for message in st.session_state.messages: # Display the prior chat messages
    with st.chat_message(message["role"]):
        st.write(message["content"])

# If last message is not from assistant, generate a new response
if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = st.session_state.chat_engine.query(prompt)    
            st.write(response.response)
            message = {"role": "assistant", "content": response.response}
            st.session_state.messages.append(message) # Add response to message history
