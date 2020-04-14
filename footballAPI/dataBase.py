import time

from .core import *

class dataBase(object):
    def __init__(self, db, ordered):
        self.dbConnect = db
        self.ordered = ordered

    def processing(self, sec = None):
        # Importation of the data in data base
        print("Start of data importation in PostgreSQL")
        # Condition for know if there are data in 'sec' argument, if it the case it is ths under base, it is not the main call of processing function
        if sec != None:
            dataValue = sec
        else:
            dataValue = self.ordered
        firstP = 1

        # Loop for processing all data
        for i in list(dataValue.values())[0]:
            index = 0
            createTable = "CREATE TABLE IF NOT EXISTS "+list(dataValue.keys())[0]+"( id serial, "

            if firstP == 1:
                # Base create for insert and delete command
                instert = " Insert into " + list(dataValue.keys())[0] + "("
                baseNet = "DELETE FROM " + list(dataValue.keys())[0] + " WHERE id IN (Select tab2.id FROM " + list(dataValue.keys())[0] + " AS tab1, "  + list(dataValue.keys())[0] + " AS tab2 Where "

                # Loop for creating the table with sql command Create Table
                for j in i.keys():
                    # Request creation
                    createTable = createTable + str(j) +' varchar,'
                    instert = instert + str(j) + ' ,'
                    baseNet = baseNet +"tab1." + str(j) + " = tab2."+ str(j) +" and "
                createTableF = createTable[0:-1] + " )"
                baseNet = baseNet +  " tab1.id <> tab2.id AND tab1.id=(SELECT min(id) FROM " +list(dataValue.keys())[0]+ " as tab WHERE "
                for jj in i.keys():
                    baseNet = baseNet +"tab1." + str(jj) + " = tab."+ str(jj) +" and "
                baseNet = baseNet[0:-4] + "))"
                instert = instert[0:-1] + ") VALUES "
                firstP = 0
            instert = instert + " ("

            # Loop for data insert with data in
            for data in i.values():
                if type(data) is list:
                    k = list(i.keys())[index]
                    val = {k : data}
                    self.processing(val)
                    req = "(Select " + k + ".id From " + k + " Where "
                    for u in data[0].keys():
                        req = req + k  + "."+ u + " like '"+ str(data[0][u]) + "' and "
                    req = req[0:-4] + " limit 1)"
                    instert= instert + req + ' ,'

                else:
                    instert= instert +'\'' +str(data) +'\''+ ' ,'

                index += 1
            instert = instert[0:-1] + "),"

        # Request execution
        cur = self.dbConnect.cursor()
        cur.execute(createTableF)
        cur.execute(instert[0:-1])
        cur.execute(baseNet)
        cur.close()
        self.dbConnect.commit()
        print("End of data importation")