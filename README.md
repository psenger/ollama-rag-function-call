# Ollama RAG - Consistent JSON Responses from AI

> Unlocking Consistent AI Outputs with JSON Formatting for Seamless Integrations

## Introduction:

Welcome to the Ollama RAG Function Call demo! 

This project showcases how to reliably interact with an AI model to receive consistent, well-structured JSON responses. 
By enforcing a predefined schema and using a clear communication protocol, this demo ensures that AI-generated data, 
such as city names and geographical coordinates, is always formatted correctly. You'll learn how to set up a Python 
environment that communicates with the AI model and generates predictable, schema-compliant outputs, enabling smoother 
and more reliable AI integration into your applications.

## Assumptions

1. You have python 3 on your computer
2. you have Ollama installed on your computer or can access it.
3. you have installed a model, and know how to edit files.

## Instructions for Setting Up and Running the Project

Follow these steps to download the project from GitHub, set up a virtual environment, install dependencies, and run the project.

### 1. Download the Project from GitHub

1. Open your terminal (or command prompt) on your machine.
2. Navigate to the directory where you want to download the project:
   ```bash
   cd /path/to/your/directory
   ```
3. Clone the GitHub repository:
   ```bash
   git clone https://github.com/psenger/ollama-rag-function-call.git
   ```
4. Change directory into the project folder:
   ```bash
   cd ollama-rag-function-call
   ```

### 2. Create a Virtual Environment

1. Create a virtual environment inside the project folder:
   ```bash
   python3 -m venv .venv
   ```
   
2. Activate the virtual environment:
   - **On macOS/Linux:**
     ```bash
     source .venv/bin/activate
     ```
   - **On Windows:**
     ```bash
     .\.venv\Scripts\activate
     ```

### 3. Install the Dependencies

1. Once the virtual environment is activated, install the required dependencies listed in the `requirements.txt` file:
   ```bash
   pip install -r requirements.txt
   ```

### 4. Create the .env File

1. In the root of the project directory, create a new file named `.env`.
 
2. Open the `.env` file and add the following content:

``` 
API_URL="http://localhost:11434/api/chat"
AI_MODEL="llama3.1:8b"
```

These environment variables define the API endpoint for the AI model and the model version to use.

### 5. Start the Project

1. After installing the dependencies, follow the project documentation (usually in `README.md`) for any specific startup instructions. Typically, you might need to run a Python script or start a server.

2. For example, if there is a `main.py` file, you could start it like this:
   ```bash
   python main.py
   ```

### Summary of Commands

```bash

## Step 1: Clone the repository
git clone https://github.com/psenger/ollama-rag-function-call.git
cd ollama-rag-function-call

## Step 2: Create and activate the virtual environment
python3 -m venv .venv
source .venv/bin/activate   # For macOS/Linux
## or
.\.venv\Scripts\activate    # For Windows

## Step 3: Install dependencies
pip install -r requirements.txt

## Step 4: Run the project (example)
python main.py
```
