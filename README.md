### **Project Overview**

This project is a simple FastAPI application designed to manage a bookstore. It allows you to create, read, update, and delete books.

### **Project Structure**

* **`bookstore/`:** Root directory of the project.
    * **`app/`:** Contains the FastAPI application code.
        * **`main.py`:** Entry point of the application, defines routes and handlers.
        * **`models.py`:** Defines data models to represent books.
        * **`utils.py`:** Contains utility functions, such as handling JSON files.
    * **`data/`:** Contains data, including the `books.json` file which stores the list of books.
    * **`requirements.txt`:** Lists the project's dependencies.
    * **`.env`:** File for storing environment variables (optional).

### **Installation**

1. **Clone the repository**
   ```bash
   git clone https://github.com/hervenzoghe/bookstore-api.git


2. **Create a virtual environment (recommended)**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Linux/macOS

3. **Install dependencies**

pip install -r requirements.txt

4. **Running the application locally**
    ```bash
    uvicorn app.main:app --reload

5. **Using the API**

You can Get a book by ID/author/genre/***

```
curl http://127.0.0.1:8000/books 
```