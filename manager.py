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