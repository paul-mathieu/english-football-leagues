from .core import *

class dataBase(object):
    def __init__(self, db):
        self.dbConnect = db

    def cc(self):
        print(self.dbConnect)