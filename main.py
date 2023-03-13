import os
import json
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


private_key_id = os.environ.get('FB_PRIVATE_KEY_ID')
private_key = os.environ.get('FB_PRIVATE_KEY')

with open("key.json") as json_file:
    key_file = json.load(json_file)
    json_file.close()

with open("/tmp/key.json", "w", encoding='utf-8') as json_file:
    key_file['private_key_id'] = private_key_id
    key_file['private_key'] = private_key
    json_object = json.dumps(key_file, ensure_ascii=False, indent=4)
    json_file.write(json_object)
    json_file.close()

cred = credentials.Certificate("/tmp/key.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://get-got-bot-default-rtdb.europe-west1.firebasedatabase.app/e"
})


def get_poem(user_id, user_type):
    ref = db.reference("/test")
    return ref.get()
