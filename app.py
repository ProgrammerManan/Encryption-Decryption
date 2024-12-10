from flask import Flask, render_template, request, jsonify
import base64

app = Flask(__name__)

"""CAESAR CIPHER FUNCTION"""
def caesar_cipher(text, key, encrypt=True):
    result = ""
    key = int(key)
    if not encrypt:
        key = -key
    #Implement a list
    for char in text:
        if char.isalpha():
            """
            65 is the ASCII value of 'A' (uppercase)
            97 is the ASCII value of 'a' (lowercase)
            ensures that uppercase and lowercase letters are handled separately
            """
            shift = 65 if char.isupper() else 97
            result += chr((ord(char) - shift + key) % 26 + shift)
        else:
            result += char
    return result

"""VIGENERE CIPHER FUNCTION"""
def vigenere_cipher(text, keyword, encrypt=True):
    result = []
    keyword = keyword.lower()
    keyword_length = len(keyword)
    keyword_as_int = [ord(k) - 97 for k in keyword]
    text_as_int = [ord(c) for c in text]

    #ASCII
    for i, char in enumerate(text_as_int):
        if 65 <= char <= 90 or 97 <= char <= 122:  #check if the character is a letter
            is_upper = 65 <= char <= 90
            shift = keyword_as_int[i % keyword_length]
            shift = shift if encrypt else -shift
            base = 65 if is_upper else 97
            result.append(chr((char - base + shift) % 26 + base))
        else:
            result.append(chr(char))  # non-alphabetic characters remain unchanged (@, #, $, etc)
    return ''.join(result)

"""BASE64 FUNCTION"""
def base64_transform(text, encode=True):
    if encode:
        return base64.b64encode(text.encode()).decode()
    else:
        try:
            return base64.b64decode(text.encode()).decode()
        except Exception as e:
            return "Invalid Base64 string"

"""
BACON CIPHER
"""
def bacon_cipher_encrypt(text):
    """
    encrypts a plaintext message using the Bacon Cipher (letter 1: A, letter 2: B)
    """
    bacon_dict = {
        'A': 'AAAAA', 'B': 'AAAAB', 'C': 'AAABA', 'D': 'AAABB', 'E': 'AABAA',
        'F': 'AABAB', 'G': 'AABBA', 'H': 'AABBB', 'I': 'ABAAA', 'J': 'ABAAB',
        'K': 'ABABA', 'L': 'ABABB', 'M': 'ABBAA', 'N': 'ABBAB', 'O': 'ABBBA',
        'P': 'ABBBB', 'Q': 'BAAAA', 'R': 'BAAAB', 'S': 'BAABA', 'T': 'BAABB',
        'U': 'BABAA', 'V': 'BABAB', 'W': 'BABBA', 'X': 'BABBB', 'Y': 'BBAAA',
        'Z': 'BBAAB'
    }
    text = text.upper()
    encrypted = ' '.join(bacon_dict.get(char, char) for char in text if char.isalpha())
    return encrypted

def bacon_cipher_decrypt(ciphertext):
    """
    decrypts a Bacon Cipher message (letter 1: A, letter 2: B)
    """
    bacon_dict = {
        'AAAAA': 'A', 'AAAAB': 'B', 'AAABA': 'C', 'AAABB': 'D', 'AABAA': 'E',
        'AABAB': 'F', 'AABBA': 'G', 'AABBB': 'H', 'ABAAA': 'I', 'ABAAB': 'J',
        'ABABA': 'K', 'ABABB': 'L', 'ABBAA': 'M', 'ABBAB': 'N', 'ABBBA': 'O',
        'ABBBB': 'P', 'BAAAA': 'Q', 'BAAAB': 'R', 'BAABA': 'S', 'BAABB': 'T',
        'BABAA': 'U', 'BABAB': 'V', 'BABBA': 'W', 'BABBB': 'X', 'BBAAA': 'Y',
        'BBAAB': 'Z'
    }
    # Split the ciphertext into 5-character chunks
    ciphertext = ciphertext.replace(" ", "")
    chunks = [ciphertext[i:i+5] for i in range(0, len(ciphertext), 5)]
    print(chunks)
    decrypted = ''.join(bacon_dict.get(chunk, '?') for chunk in chunks)
    return decrypted

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
    app.run(debug=True, host="192.168.1.175")
