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
        self.path = path
        with open(path, "rb") as f:
            self.content = f.read()
            dec_salt = self.content[16:136]
            self.salt = self.content[0:16]
            if Fernet(self.pw_to_key(password)).decrypt(dec_salt) != self.salt:
                return
            self.db = Database(self.content[136:])
            if self.content[136:]:
                self.db.decr(self.pw_to_key(password))
            self.db.decomp()

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
    
    def savedb(self, password, path=False):
        if not path:
            path = self.path #"save" if no path is specified, otherwise "save as"
        self.db.recomp()
        self.db.encr(self.pw_to_key(password))
        with open(self.path, "rb") as f:
            copy = f.read()
            if Fernet(self.pw_to_key(password)).decrypt(copy[16:136]) != self.salt: #check if key is correct
                return #return if the key is wrong
        self.content = self.content[:136] + self.db.content
        with open(path,"wb") as f:
            f.write(self.content)
        return

class Database():
    def __init__(self, content, isEncr = True):
        self.entries = list()
        self.content = content
        self.isEncr = isEncr

    def decr(self, key):
        self.content = Fernet(key).decrypt(self.content)
        self.isEncr = False

    def encr(self, key):
        self.content = Fernet(key).encrypt(bytes(self.content, "utf-8"))
        self.isEncr = True

    def decomp(self):
        if self.content:
            split = self.content.split(b"::")
            self.entries = list()
            for x in split:
                x = x.split(b":")
                self.entries.append({"id":int(x[0]),"name":str(x[1], "utf-8"),"email":str(x[2],"utf-8"),"pw":str(x[3], "utf-8")})
    
    def recomp(self):
        content = "" #reset content as a decompiled updated copy exists in self.entries
        for x in self.entries:
            content += f"::{x['id']}:{x['name']}:{x['email']}:{x['pw']}"
        self.content = content[2:]

    def add_entry(self, name, email, pw):
        if not self.entries:
            id = 0
        else:
            id = self.entries[-1]["id"] + 1
        self.entries.append({"id":id,"name":name,"email":email,"pw":pw})
        return

    def del_entry(self, id):
        for x in self.entries:
            if x["id"] == id:
                self.entries.remove(x)
                return #there should not be more than 1 match
        return "no matches"

    def get_entry(self, id):
        for x in self.entries:
            if x["id"] == id:
                return x

    def edit_entry(self, id, new_entry:dict):
        for i in range(len(self.entries)):
            if self.entries[i]["id"] == id:
                self.entries[i] = new_entry
                return

def cr_ex_db():#create example database
    man = PwManager()
    man.createdb("path", "password")
    man.opendb("path", "password")
    man.db.add_entry("name1", "email1", "pw1")
    man.db.add_entry("name2", "email2", "pw2")
    man.db.add_entry("name3", "email3", "pw3")
    man.savedb("password")