import os
import json
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


key = os.environ.get('FIREBASE_KEY')
json_object = json.dumps(json.loads(key), indent=4)
with open("key.json", "w") as outfile:
    outfile.write(json_object)

#cred = credentials.Certificate("get-got-bot-firebase-adminsdk-6m5xd-a9b647bce5.json")
cred = credentials.Certificate("key.json")
app = firebase_admin.initialize_app(cred, {
    'databaseURL': "https://get-got-bot-default-rtdb.europe-west1.firebasedatabase.app/e"
})


def get_poem(user_id, user_type):
    ref = db.reference("/test")
    return ref.get()
