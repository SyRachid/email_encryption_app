import os
import json
import base64

KEYS_FILE = 'keys.json'

def generate_key():
    return os.urandom(16)

def save_key(key_id, key):
    if not os.path.exists(KEYS_FILE):
        with open(KEYS_FILE, 'w') as file:
            json.dump({}, file)

    with open(KEYS_FILE, 'r') as file:
        keys = json.load(file)

    keys[key_id] = base64.b64encode(key).decode('utf-8')

    with open(KEYS_FILE, 'w') as file:
        json.dump(keys, file)

def load_key(key_id):
    with open(KEYS_FILE, 'r') as file:
        keys = json.load(file)

    return base64.b64decode(keys[key_id])

def delete_key(key_id):
    with open(KEYS_FILE, 'r') as file:
        keys = json.load(file)

    if key_id in keys:
        del keys[key_id]

    with open(KEYS_FILE, 'w') as file:
        json.dump(keys, file)
