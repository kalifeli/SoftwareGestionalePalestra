import firebase_admin
from firebase_admin import credentials, firestore 

cred = credentials.Certificate("gymsoftware-b4745-firebase-adminsdk-fbsvc-93f6a914ba.json")
firebase_admin.initialize_app(cred)  

db_firestore = firestore.client()

def get_firestore_client():
    return db_firestore