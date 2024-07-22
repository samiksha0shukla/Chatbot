# Chatbot
Chatbot - GenAI
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
   
### 5. Configure the Data Path:
 * Copy the path of **Corpus.pdf** and paste it into the **DATA_PATH** variable on line 11 of      the **populated_database.py** file.
 * Run **populated_database.py** to populate the database.

### 6. Run the Streamlit Application:
 * Open a terminal and run the following command to start the Streamlit chatbot interface:<br>
   **streamlit run query_ui.py**

### 7. Interact with the Chatbot:
 * A web browser will open displaying the Streamlit chatbot interface.
 * Type your question in the sidebar of the interface and hit Enter. If the question is within     the context of the corpus, you will get an answer. Otherwise, you will see "please contact      the business" as the reply.
 

