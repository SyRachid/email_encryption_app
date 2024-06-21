from flask import Flask, render_template, request, jsonify
from Crypto.Cipher import AES
import base64
import os
from key_manager import generate_key, save_key, load_key, delete_key

app = Flask(__name__)

# Taille de bloc pour le padding
BS = 16

def pad(s):
    pad_len = BS - len(s) % BS
    padding = chr(pad_len) * pad_len
    return s + padding

def unpad(s):
    padding_len = ord(s[-1])
    return s[:-padding_len]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/encrypt')
def encrypt_page():
    return render_template('encrypt.html')

@app.route('/decrypt')
def decrypt_page():
    return render_template('decrypt.html')

@app.route('/perform_encrypt', methods=['POST'])
def perform_encrypt():
    try:
        raw = request.form['message']
        raw_padded = pad(raw)
        iv = os.urandom(16)
        key = generate_key()
        cipher = AES.new(key, AES.MODE_CBC, iv)
        encrypted = base64.b64encode(iv + cipher.encrypt(raw_padded.encode('utf-8'))).decode('utf-8')

        key_id = base64.b64encode(os.urandom(16)).decode('utf-8')
        save_key(key_id, key)

        return jsonify({'encrypted_message': encrypted, 'key_id': key_id})
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/perform_decrypt', methods=['POST'])
def perform_decrypt():
    try:
        enc = request.form['encrypted_message']
        key_id = request.form['key_id']
        enc = base64.b64decode(enc)
        iv = enc[:16]
        key = load_key(key_id)
        cipher = AES.new(key, AES.MODE_CBC, iv)
        decrypted = cipher.decrypt(enc[16:]).decode('utf-8')
        decrypted_unpadded = unpad(decrypted)
        delete_key(key_id)
        return jsonify({'decrypted_message': decrypted_unpadded})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
