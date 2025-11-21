import firebase_admin
from firebase_admin import credentials, firestore

# Load your Firebase service account key
cred = credentials.Certificate("admin_key.json")  # updated file name
firebase_admin.initialize_app(cred)

# Firestore client
db = firestore.client()
