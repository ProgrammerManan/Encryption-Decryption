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
