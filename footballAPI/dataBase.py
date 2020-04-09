from .core import *

class dataBase(object):
    def __init__(self, db, ordered):
        self.dbConnect = db
        self.ordered = ordered

    def processing(self):
        firstP = 1
        for i in list(self.ordered.values())[0]:
            createTable = "CREATE TABLE IF NOT EXISTS "+list(self.ordered.keys())[0]+"("

            if firstP == 1:
                inster = " Insert into " + list(self.ordered.keys())[0] + "("
                for j in i.keys():
                    createTable = createTable + str(j) +' varchar,'
                    inster = inster + str(j) + ' ,'
                createTableF = createTable[0:-1] + " )"
                inster = inster[0:-1] + ") VALUES "
                firstP = 0

            inster = inster + " ("
            for data in i.values():
                if type(data) is dict:
                    pass
                else:
                    inster= inster +'\'' +str(data) +'\''+ ' ,'

            inster = inster[0:-1] + "),"
        cur = self.dbConnect.cursor()
        cur.execute(createTableF)
        cur.execute(inster[0:-1])
        cur.close()
        self.dbConnect.commit()