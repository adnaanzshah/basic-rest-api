from flask import Flask, request, jsonify
import uuid
import re

app = Flask(__name__)

# In-memory storage for users
users = {}

# Utility function to validate email
def is_valid_email(email):
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None

# Root route
@app.route('/')
def index():
    return jsonify({"message": "Welcome to the User API. Use /users for CRUD operations."}), 200

# Create a new user
@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()

    # Basic input validation
    if not data.get('name') or not data.get('email') or not data.get('age'):
        return jsonify({"error": "Missing required fields: name, email, age"}), 400
    
    if not is_valid_email(data['email']):
        return jsonify({"error": "Invalid email format"}), 400

    try:
        age = int(data['age'])
        if age < 0:
            return jsonify({"error": "Age must be a positive number"}), 400
    except ValueError:
        return jsonify({"error": "Age must be a number"}), 400

    user_id = str(uuid.uuid4())
    user = {
        "id": user_id,
        "name": data['name'],
        "email": data['email'],
        "age": age
    }
    users[user_id] = user

    return jsonify(user), 201

# Retrieve all users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(list(users.values())), 200

# Retrieve a user by ID
@app.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    user = users.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user), 200

# Update a user by ID
@app.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    user = users.get(user_id)

    if not user:
        return jsonify({"error": "User not found"}), 404

    # Update fields with validation
    if 'name' in data:
        user['name'] = data['name']

    if 'email' in data:
        if not is_valid_email(data['email']):
            return jsonify({"error": "Invalid email format"}), 400
        user['email'] = data['email']

    if 'age' in data:
        try:
            age = int(data['age'])
            if age < 0:
                return jsonify({"error": "Age must be a positive number"}), 400
            user['age'] = age
        except ValueError:
            return jsonify({"error": "Age must be a number"}), 400

    users[user_id] = user
    return jsonify(user), 200

# Delete a user by ID
@app.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = users.pop(user_id, None)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
