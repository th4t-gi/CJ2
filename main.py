import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate('something.json')
app = firebase_admin.initialize_app(cred)
client = firestore.client(app)

print(client.collection('users')[1])
