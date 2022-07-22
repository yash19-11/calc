import mysql.connector

db = mysql.connector.connect(host = 'localhost', username = 'root', password = 'abcde')

cursor = db.cursor()

cursor.execute("CREATE DATABASE calculator")