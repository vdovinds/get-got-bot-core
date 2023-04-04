import os
import json
import ast
import random
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

private_key_id = os.environ.get('FB_PRIVATE_KEY_ID')
private_key = ast.literal_eval(os.environ.get('FB_PRIVATE_KEY'))

with open("key.json") as json_file:
    key_file = json.load(json_file)
    json_file.close()

with open("/tmp/key.json", "w") as json_file:
    key_file['private_key_id'] = private_key_id
    key_file['private_key'] = private_key
    json_object = json.dumps(key_file, ensure_ascii=False, indent=4)
    json_file.write(json_object)
    json_file.close()

cred = credentials.Certificate("/tmp/key.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://get-got-bot-default-rtdb.europe-west1.firebasedatabase.app/e"
})


def get_random_poem(user_type, user_id, user_info):
    db.reference("/users").child(f"{user_type}_{user_id}").update(
        {
            "user_info": user_info
        }
    )
    return get_random_poem_internal()


def get_random_poem_internal():
    verbs = db.reference("/verbs").get()
    poem = random.choice(verbs)

    return poem


def issue_task(user_type, user_id, user_info):
    poem = get_random_poem_internal()
    expected_verb_form = random.choice(['first', 'second', 'third'])
    task = {
        "first": poem['first'],
        "second": poem['second'],
        "third": poem['third'],
        "ru": poem['ru'],
        "expected_verb_form": expected_verb_form,
        expected_verb_form: ""
    }

    db.reference("/users").child(f"{user_type}_{user_id}").update(
        {
            "current_poem": poem,
            "expected_answer": poem[expected_verb_form],
            "expected_verb_form": expected_verb_form,
            "user_info": user_info
        }
    )

    return task


def check_task(user_type, user_id, answer):
    expected_answer = db.reference("/users").child(f"{user_type}_{user_id}").child("expected_answer").get()

    return {
        "result": str(answer).lower() == str(expected_answer).lower()
    }


def get_task_answer(user_type, user_id):
    return db.reference("/users").child(f"{user_type}_{user_id}").child("current_poem").get()