import firebase_admin
from firebase_admin import credentials, db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {"databaseURL": "https://your-project.firebaseio.com/"})

def log_waste(category):
    ref = db.reference("waste_logs")
    ref.push({"category": category})
