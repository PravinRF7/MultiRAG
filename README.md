

# Multimodal RAG Application with Gradio

This project is a multimodal Retrieval-Augmented Generation (RAG) application that integrates text embeddings, PDF data storage, and natural language querying capabilities with a user-friendly Gradio interface. It uses LangChain's embedding and retrieval capabilities with Chroma vector store to allow users to upload PDF documents, query information from them, and run predefined tests.

## Features

- **Database Population**: Upload PDFs and store the content in a vector database (Chroma) for quick access and retrieval.
- **Querying**: Submit natural language questions to search the vector database and retrieve relevant information.
- **Testing**: Run predefined tests to validate the response accuracy.


## Installation

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd project_folder
   ```

2. **Install Dependencies**
   Make sure you have Python installed, then install the required packages using:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Running the Application
To start the Gradio app, run the following command:
```bash
python gradio_app.py
```

This will launch a Gradio interface with three tabs:
1. **Reset and Populate Database**: Upload PDFs and optionally reset the database.
2. **Query Database**: Enter a question to retrieve information from the database.
3. **Run Tests**: Validate predefined queries to check for accuracy.

### Example Workflow
1. **Upload PDFs**: Go to the **Reset and Populate Database** tab, upload PDF files, and click **Populate Database**. This will process and store document content in a vector database.
2. **Query Database**: In the **Query Database** tab, type a question related to the uploaded documents and click **Submit Query** to receive an answer based on the content.
3. **Run Tests**: Navigate to the **Run Tests** tab and click **Run Tests** to execute pre-set queries and check if the results are correct.



## Dependencies

All required packages are listed in `requirements.txt`. To install them, use:
```bash
pip install -r requirements.txt
```
