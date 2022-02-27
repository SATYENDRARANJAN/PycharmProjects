#pip install pycrypto

import hashlib
from Crypto import Random
from Crypto.Cipher import AES
from base64 import b64encode, b64decode


class AESCipher(object):
    def __init__(self, key):
        self.block_size = 256
        self.key = "z5yK1lw7XYt6YKdP7Pne2Jw3zRkMAziH" #AES KEY
        self.iv="i0kbCAlFTlDXshYV" # AES INIT VECTOR

    def encrypt(self):
        plain_text = 'TOKENKEY'+"|"+"TOKENVALUE"
        cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        encrypted_text = cipher.encrypt(plain_text.encode())
        return b64encode(b64encode(encrypted_text))


