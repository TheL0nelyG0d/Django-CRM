#Install Mysql locally like go to mysql website
#pip install mysql
#pip install mysql-connector
#pip install mysql-connector-pthon


import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Arzumkuzum2134-'
)

#Prepare a cursor
cursorObject = dataBase.cursor()


# Create a database
cursorObject.execute("CREATE DATABASE dcrm")
print("All Done!")