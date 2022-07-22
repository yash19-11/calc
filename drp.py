import mysql.connector

db = mysql.connector.connect(host = "localhost", username = "root", password = "abcde", database = "calculator")

cursor = db.cursor()

seq = "DROP TABLE addition, substraction, multiplication, divide, modulus"

cursor.execute(seq)
