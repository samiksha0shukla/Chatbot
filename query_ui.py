from langchain_community.vectorstores import Chroma
from langchain.prompts import ChatPromptTemplate
from langchain_community.llms.ollama import Ollama
from langchain_core.messages import HumanMessage, AIMessage
import streamlit as st
from Embeddings import get_embedding_function 
from streamlit_chat import message  

CHROMA_PATH = "chroma"
PROMPT_TEMPLATE = """
You are an AI, you answer questions with appropriate answers.

Based on the following context, answer the question in detail. If you can't answer the question, only reply "Please contact the business" and nothing else:

{context}

---

Now, considering the above context, answer the following question: {question}
"""

db = None
chat_history = []
llm = Ollama(model="llama3")

def main():
    st.set_page_config(page_title="Chatbot", page_icon="🤖")
    print("Initializing Chroma...")
    embedding_function = get_embedding_function()
    global db
    db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embedding_function)
    print("Chroma initialized.")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    st.header("Chatbot 🤖")

    with st.sidebar:
        user_input = st.text_input("Your message: ")

        if user_input:
            st.session_state.messages.append(HumanMessage(content=user_input.strip()))
            with st.spinner("Thinking..."):
                response = query_rag(user_input.strip())
            st.session_state.messages.append(AIMessage(content=response))

    messages = st.session_state.get('messages', [])
    for i, msg in enumerate(messages):
        if isinstance(msg, HumanMessage):
            message(msg.content, is_user=True, key=f"{i}_user")
        elif isinstance(msg, AIMessage):
            message(msg.content, is_user=False, key=f"{i}_ai")

def query_rag(question_text: str):
    print("Searching the DB...")
    global db
    results = db.similarity_search_with_score(question_text, k=2)
    print("DB search complete.")

    context_text = "\n\n---\n\n".join([doc.page_content for doc, _score in results])
    print("Context text prepared.")

    prompt = PROMPT_TEMPLATE.format(context=context_text, question=question_text)
    print("Prompt generated.")

    response_text = llm.invoke(prompt)
    print("Model invocation complete.")

    return response_text

if __name__ == "__main__":
    main()
