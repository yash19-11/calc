import mysql.connector
import math

def calculator():

    db = mysql.connector.connect(host = "localhost", username = "root", password = "abcde", database = "calculator")

    cursor = db.cursor()

    choice = input("enter your choice = a / s / m / d / mod / sqr:")

    num1 = float(input("enter the first number:"))
    num2 = float(input("enter the second number:"))


    if choice == 'a':
     
        sum = num1 + num2 
        print(sum)
        seq = "INSERT INTO addition(A, B, sum) VALUES (%s, %s, %s)"
        val = (num1, num2, sum)
        cursor.execute(seq, val)

    elif choice == 's':

        res = num1 - num2
        print(res)
        seq = "INSERT INTO substraction(A, B, result) VALUES (%s, %s, %s)"
        val = (num1, num2, res)
        cursor.execute(seq,val)

    elif choice == 'm':

        product = num1 * num2
        print(product)
        seq = "INSERT INTO multiplication(A, B, product) VALUES (%s, %s, %s)"
        val = (num1, num2, product)
        cursor.execute(seq,val)
 
    elif choice == 'd':

        resl = num1/num2
        print(resl)
        seq = "INSERT INTO divide(A, B, result) VALUES (%s, %s, %s)"
        val = (num1, num2, resl)
        cursor.execute(seq,val)

    elif choice == 'mod':
        
        answer = num1 % num2
        print(answer)
        seq = "INSERT INTO modulus(A, B, result) VALUES (%s, %s, %s)"
        val = (num1, num2, answer)
        cursor.execute(seq,val)

    elif choice == 'sqr':

       ans_1 = math.sqrt(num1)
       ans_2 = math.sqrt(num2)
       print(ans_1)
       print(ans_2)
   
       seq = "INSERT INTO square_root(A, B, answer_1, answer_2) VALUES (%s, %s, %s, %s)"
       val = (num1, num2, ans_1, ans_2)
       cursor.execute(seq,val)

    else:
        print("invalid!")

    db.commit()
    cal_again()

def cal_again():

    again = input("do you want to continue?: Y or N = ")
    
    if again == "Y":
        calculator()
    elif again == "N":
        print("bye!")
    else:
        cal_again()

calculator()