from flask import Flask, request, jsonify

app = Flask(__name__)

# Simulated user data (replace with actual user database)
users = {
    "student": {"username": "akshith", "password": "pass"},
    "admin": {"username": "admin_user", "password": "admin_password"},
    "company": {"username": "company_user", "password": "company_password"}
}

@app.route("/login/<role>", methods=["POST"])
def login(role):
    login_data = request.form

    if role not in users:
        return jsonify({"message": "Invalid role"}), 400

    stored_user = users[role]
    if login_data["username"] == stored_user["username"] and login_data["password"] == stored_user["password"]:
        return jsonify({"message": "Login successful"}), 200
    else:
        return jsonify({"message": "Invalid credentials"}), 401

if __name__ == "__main__":
    app.run(port=5000)
