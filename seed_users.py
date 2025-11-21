from firebase_config import db

# List of sample users
users = [
    {"id": "u001", "name": "Apeksha Jadhav"},
    {"id": "u002", "name": "Rohan Patil"},
    {"id": "u003", "name": "Priya Singh"},
    {"id": "u004", "name": "Amit Sharma"},
    {"id": "u005", "name": "Sneha Rao"}
]

def insert_users():
    for user in users:
        db.collection("users").document(user["id"]).set(user)
    print("Users added successfully.")

if __name__ == "__main__":
    insert_users()
