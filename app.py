import firebase_admin
from firebase_admin import credentials,firestore

cred = credentials.Certificate('service_key.json')

app = firebase_admin.initialize_app(cred)

db = firestore.client()

main_collection_ref = db.collection('User').stream() 

for doc in main_collection_ref:
    #
    user_collection_ref = db.collection('Users').document(doc.id).collections()
    print(doc.id)
    res = doc.to_dict()
    print(res['question'])
    