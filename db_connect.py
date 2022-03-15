import mysql.connector

############# CONNECTION TO THE DATABASE ###################

def _db_connect():
    db = mysql.connector.connect(host="localhost",user="root",password="1234",database="tweeterdb")
    print(db)

    ############ SETTING UP THE CONNECTION #####################
