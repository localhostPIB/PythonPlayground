import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="myPythondatabase"
)

cursor = mydb.cursor()

# cursor.execute("CREATE DATABASE myPythondatabase")

sql_anweisung = """
CREATE TABLE personen (
vorname VARCHAR(20), 
nachname VARCHAR(30), 
geburtstag DATE
);"""

nachname = "Krueger"
vorname = "Freddy"
geburtstag = "1947-07-06"
cursor.execute("""
                INSERT INTO personen 
                       VALUES (%s, %s, %s)
               """,
               (vorname, nachname, geburtstag)
               )

cursor.close()

mydb.close()
