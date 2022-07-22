import mysql.connector

db = mysql.connector.connect(host = "localhost", username = "root", password = "abcde", database = "calculator")

cursor = db.cursor()

cursor.execute("CREATE TABLE addition(a float, b float, sum float)")

cursor.execute("CREATE TABLE substraction(a float, b float, result float)")

cursor.execute("CREATE TABLE multiplication(a float, b float, product float)")
 
cursor.execute("CREATE TABLE divide(a float, b float, result float)")

cursor.execute("CREATE TABLE modulus(a float, b float, result float)")

cursor.execute("CREATE TABLE square_root(a float, b float, answer_1 float, answer_2 float)")