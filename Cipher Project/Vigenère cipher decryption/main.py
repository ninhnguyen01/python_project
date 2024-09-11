# Import the encryption file for decryption
from encrypt import *

# Decrypt the imported file
def decrypt(message, key):
    return vigenere(message, key, -1)

decryption = decrypt(text, custom_key)
print(f'\nDecrypted text: {decryption}\n')