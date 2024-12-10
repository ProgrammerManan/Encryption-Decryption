from flask import Flask, render_template, request, jsonify

"""
BACKEND FUNCTION IMPORTS TO MANAGE COMPLEXITY
"""
from backend.caeser import caesar_cipher
from backend.vigenere import vigenere_cipher
from backend.base64 import base64_transform
from backend.bacon import bacon_cipher_decrypt, bacon_cipher_encrypt

app = Flask(__name__)

"""
APP ROUTES FOR PAGES
"""
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/caeser")
def caeser():
    return render_template("caeser.html")

@app.route("/base64")
def base64():
    return render_template("base64.html")

@app.route("/vigenere")
def vigenere():
    return render_template("vigenere.html")

@app.route("/bacon")
def bacon():
    return render_template("bacon.html")

"""
APP PROCESSES TO GET DATA FROM FRONTEND, PROCESS AND SEND BACK BACKEND PROCESS
"""
@app.route("/process_caesar", methods=["POST"])
def process_caesar():
    data = request.get_json()
    message = data.get("message", "")
    key = data.get("key", 1)
    operation = data.get("operation", "encrypt")

    if operation == "encrypt":
        result = caesar_cipher(message, key, encrypt=True)
    elif operation == "decrypt":
        result = caesar_cipher(message, key, encrypt=False)
    else:
        result = "Invalid operation"

    return jsonify({"result": result})


@app.route("/process_base64", methods=["POST"])
def process_base64():
    data = request.get_json()
    message = data.get("message", "")
    operation = data.get("operation", "encode")

    if operation == "encode":
        result = base64_transform(message, encode=True)
    elif operation == "decode":
        result = base64_transform(message, encode=False)
    else:
        result = "Invalid operation"

    return jsonify({"result": result})

@app.route("/process_vigenere", methods=["POST"])
def process_vigenere():
    data = request.get_json()
    message = data.get("message", "")
    key = data.get("key", "")
    operation = data.get("operation", "encrypt")

    if not key.isalpha():
        return jsonify({"result": "Keyword must contain only alphabetic characters."})

    if operation == "encrypt":
        result = vigenere_cipher(message, key, encrypt=True)
    elif operation == "decrypt":
        result = vigenere_cipher(message, key, encrypt=False)
    else:
        result = "Invalid operation"

    return jsonify({"result": result})

@app.route("/process_bacon", methods=["POST"])
def process_bacon():
    data = request.get_json()
    message = data.get("message", "")
    operation = data.get("operation", "encrypt")

    if operation == "encrypt":
        result = bacon_cipher_encrypt(message)
    elif operation == "decrypt":
        result = bacon_cipher_decrypt(message)
    else:
        result = "Invalid operation"

    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(debug=True)
