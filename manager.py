from os import urandom
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
from cryptography.fernet import Fernet
import base64
class PwManager():
    def __init__(self):
        pass

    def opendb(self, path, password):
        with open(path, "rb") as f:
            self.content = f.read()
            dec_salt = self.content[16:136]
            self.salt = self.content[0:16]
            if Fernet(self.pw_to_key(password)).decrypt(dec_salt) != self.salt:
                return
            self.db = Database(self.content[136:])
            self.db.decr(self.pw_to_key(password))

    def createdb(self, path, password):
        open(path, "x")
        with open(path, "wb") as f:
            self.salt = urandom(16)
            f.write(self.salt+Fernet(self.pw_to_key(password)).encrypt(self.salt)) #write salt at the start of file
    
    def pw_to_key(self, password):
        backend = default_backend()

        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=self.salt,
            iterations=100000,
            backend=backend
        )
        key = base64.urlsafe_b64encode(kdf.derive(bytes(password, "utf-8")))
        return key

class Database():
    def __init__(self, content, isEncr = True):
        self.content = content
        self.isEncr = isEncr

    def decr(self, key):
        self.content = Fernet(key).decrypt(self.content)
        self.isEncr = False

    def encr(self, key):
        self.content = Fernet(key).encrypt(self.content)
        self.isEncr = True

    def add_entry(self):
        pass

    def del_entry(self):
        pass

    def edit_entry(self):
        pass