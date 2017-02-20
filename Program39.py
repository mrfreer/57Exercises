import pymysql
import datetime

conn = pymysql.connect(host='localhost', port=3306, user='david', passwd ='david', db='dave')
cur = conn.cursor()


def displayinfo():
    cur.execute("SELECT * FROM employee")
    row = cur.fetchall()
    for i in row:
        curemp = ""
        for j in i:
            if isinstance(j, datetime.date):
                curemp = curemp + "\t" + datetime.datetime.strftime(j, '%Y-%m-%d')
            else:

                curemp = curemp + "\t" + j + "\t"
        print(curemp)

def displayindividual(name):
    cur.execute("SELECT * FROM employee WHERE first ='" + name + "'")
    row = cur.fetchall()
    for i in row:
        curemp = ""
        for j in i:
            if isinstance(j, datetime.date):
                curemp = curemp + "\t" + datetime.datetime.strftime(j, '%Y-%m-%d')
            else:

                curemp = curemp + "\t" + j + "\t"
        print(curemp)


def insert():
    first = input("Insert the first name:")
    last = input("Insert the last name:")
    job = input("Insert the job:")
    hiredate = input("Insert the YEAR-MONTH-DATE (YYYY-MM-DD):")
    cur.execute("INSERT INTO employee (first, last, position ,separation) VALUES ('" + first + "','" + last + "','" + job + "','" + hiredate + "')")
    conn.commit()


while True:
    while True:
        try:
            a = input("Enter 1 to display all the data.  Enter 2 to insert the data.  Enter 3 to view individual employees.")
        except ValueError:
            print("Must be a number.")
            continue
        else:
            if a == "1":
                print("Here")
                displayinfo()
            elif a == "2":
                insert()
            elif a == "3":
                tocheck = input("Enter a first name to check.")
                displayindividual(tocheck)
        break
    b = input("Enter quit to stop")
    if b == "quit":
        break

