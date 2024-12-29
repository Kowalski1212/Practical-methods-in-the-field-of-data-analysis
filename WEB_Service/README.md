# LLM Backend Service

## Project Description

This project is a backend service for searching and filtering large language models (LLMs). The service provides an API for searching models based on various filters, such as name, description, price, and availability. It uses FastAPI for creating the web service and PostgreSQL for storing model data.

## Purpose

The project was developed to provide access to information about language models through an API. It can be integrated with various frontend applications, such as websites or mobile apps, where searching for models with filtering options like price, availability, and description is needed.

## How to Run the Project

1. **Clone the repository:**

    ```bash
    git clone https://github.com/Kowalski1212/Practical-methods-in-the-field-of-data-analysis/tree/main/WEB_Service
    cd llm-backend-service
    ```

2. **Create and activate a virtual environment (required for Python):**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use venv\Scripts\activate
    ```

3. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Set up PostgreSQL database.**

    - Ensure you have PostgreSQL installed and configured.
    - Create a database and use the `PostGre.sql` script to create the required tables.

5. **Run the server:**

    ```bash
    uvicorn main:app --reload
    ```

    The server will be available at: `http://127.0.0.1:8000`

## Example API Request

To filter language models, you can make HTTP GET requests with various parameters. Example request:

GET http://127.0.0.1:8000/filter_models?name=Model A&minPrice=50&availability=true
 
 Example response:

```json
[
  {
    "name": "Model A",
    "description": "A large language model with advanced NLP capabilities"
  }
]
