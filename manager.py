from os import urandom
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
from cryptography.fernet import Fernet
import base64
class PwManager():
    def __init__(self):
        pass

    def opendb(self, path):
        with open(path, "r") as f:
            self.salt = f.read[0:16]
            self.db = f.read()[16:]

    def createdb(self, path):
        open(path, "x")
        self.opendb(path)
    
    def pw_to_key(self, password):
        backend = default_backend()

        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=self.salt,
            iterations=100000,
            backend=backend
        )
        key = base64.urlsafe_b64encode(kdf.derive(bytes(password)))
        return key