# Chatbot
Chatbot - GenAI  

This chatbot uses advanced technologies to answer questions based on a PDF document. It employs **Retrieval-Augmented Generation (RAG)** to combine information retrieval with text generation, enhancing responses. The chatbot utilizes the **Llama 3** (a completely free and open source LLM model) from **Ollama** for understanding and generating human-like text. **Langchain** integrates various data sources for document processing, while **Chroma** stores and retrieves document chunks efficiently. The user-friendly interface is created with **Streamlit**, allowing seamless interaction. Together, these technologies enable the chatbot to provide accurate, context-aware answers.<br>

## How to Run the Chatbot Code  
Follow these steps to set up and run the chatbot:  

### 1. Create a New Folder:  
 * Open VS Code and create a new folder for the project.

### 2. Open VS Code and create a new folder for the project.  
 * Within the new folder, create and activate a virtual environment.

### 3. Upload Project Files:

  * Upload the following files into the folder:
    * Corpus.pdf
    * Embeddings.py
    * populated_database.py
    * query_ui.py
    * requirements.txt

### 4. Install Required Packages:
 * Install all required packages by running the following command:<br>
   **pip install -r requirements.txt**

### 5. Run Llama 3 locally:  
 * Download Ollama: Get the Ollama software from: https://ollama.com/download
 * Open PowerShell: Launch PowerShell on your machine.
 * Run Ollama: Execute the following command to start Ollama:<br>
   **ollama**
 * Download Llama 3: Pull the Llama 3 model by running:<br>
   **ollama pull llama3**
 * Download nomic-embed-text: Pull the nomic-embed-text model by running:<br>
   **ollama pull nomic-embed-text**
   
### 6. Configure the Data Path:
 * Copy the path of **Corpus.pdf** and paste it into the **DATA_PATH** variable on line 11 of      the **populated_database.py** file.
 * Run **populated_database.py** to populate the database.

### 7. Run the Streamlit Application:
 * Open a terminal and run the following command to start the Streamlit chatbot interface:<br>
   **streamlit run query_ui.py**

### 8. Interact with the Chatbot:
 * A web browser will open displaying the Streamlit chatbot interface.
 * Type your question in the sidebar of the interface and hit Enter. If the question is within     the context of the corpus, you will get an answer. Otherwise, you will see "please contact      the business" as the reply.
 

