import requests

url = "http://127.0.0.1:5000/users"
payload = {
    "name": "John Doe",
    "email": "john.doe@example.com",
    "age": 30
}

response = requests.post(url, json=payload)
print(response.json())
