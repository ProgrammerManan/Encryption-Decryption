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
