# Basic REST API with Flask

This project is a basic REST API built using Flask for managing user data with CRUD operations.

## Features
- **Create** a new user.
- **Read** user data (all users or by ID).
- **Update** user data.
- **Delete** a user.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/adnaanzshah/basic-rest-api.git

2. Navigate to Project Directory:
   ```bash
   cd basic-rest-api

3. Create and Activate Virtual Environment:
   ```bash
   python -m venv env
   env\Scripts\activate

## Requirements

This project requires the following Python package:

- **Flask**
- **Requests**

To install the required dependencies, run:
```bash
pip install -r requirements.txt
```

## Running the flask Application
   ```bash
   python main.py
```
### The app will run on http://127.0.0.1:5000/

To test the API, you can use the `test_api.py` script, which sends a POST request to create a new user.

### Example of `test_api.py`:
```python
import requests

url = "http://127.0.0.1:5000/users"
payload = {
    "name": "John Doe",
    "email": "john.doe@example.com",
    "age": 30
}

response = requests.post(url, json=payload)
print(response.json())
```

Run the script with:
```bash
python test_api.py
```


