import firebase_admin
from firebase_admin import credentials
from firebase_admin import  firestore

cred = credentials.Certificate("firebase-sdk.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

user_ref = db.collection("user")
docs = user_ref.stream()

for doc in docs:
    print('{} => {} '.format(doc.id, doc.to_dict()))


