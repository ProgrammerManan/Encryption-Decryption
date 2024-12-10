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