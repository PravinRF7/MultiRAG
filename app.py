


import gradio as gr
import os
from populate_database import main as populate_main
from query_data import query_rag
from Test_rag import test_monopoly_rules, test_ticket_to_ride_rules


# Function to handle database reset and file uploads
def reset_and_populate_database(reset, pdf_files):
    # Save uploaded PDF files to the 'data' folder
    if not os.path.exists('data'):
        os.makedirs('data')

    for pdf_file in pdf_files:
        pdf_path = os.path.join('data', pdf_file.name)
        with open(pdf_path, "wb") as f:
            f.write(pdf_file.read())
    
    # Run the database reset and population
    args = []
    if reset:
        args.append("--reset")
    populate_main()

    return "Database has been reset and populated with uploaded documents."


# Function to query the database
def query_database(question):
    response_text = query_rag(question)
    return response_text


# Function to run the tests
def run_tests():
    monopoly_result = test_monopoly_rules()
    ticket_to_ride_result = test_ticket_to_ride_rules()
    return f"Monopoly Rules Test: {'Passed' if monopoly_result else 'Failed'}\nTicket to Ride Rules Test: {'Passed' if ticket_to_ride_result else 'Failed'}"


# Create Gradio interface
with gr.Blocks() as demo:
    gr.Markdown("# Multimodal RAG Application")

    with gr.Tab("Reset and Populate Database"):
        reset = gr.Checkbox(label="Reset Database", value=False)
        pdf_files = gr.File(label="Upload PDFs", file_types=["pdf"], file_count="multiple")
        populate_button = gr.Button("Populate Database")
        populate_output = gr.Textbox(label="Output")
        populate_button.click(fn=reset_and_populate_database, inputs=[reset, pdf_files], outputs=populate_output)

    with gr.Tab("Query Database"):
        question = gr.Textbox(label="Enter your query", placeholder="Ask a question...")
        query_button = gr.Button("Submit Query")
        query_output = gr.Textbox(label="Query Response")
        query_button.click(fn=query_database, inputs=question, outputs=query_output)

    with gr.Tab("Run Tests"):
        test_button = gr.Button("Run Tests")
        test_output = gr.Textbox(label="Test Results")
        test_button.click(fn=run_tests, inputs=[], outputs=test_output)

# Launch the Gradio app
demo.launch(debug=True)
