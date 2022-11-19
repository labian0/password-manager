class PwManager():
    def __init__(self):
        pass

    def opendb(self, path):
        self.db = open(path, "r")
    
    def createdb(self, path):
        open(path, "x")
        self.opendb(path)