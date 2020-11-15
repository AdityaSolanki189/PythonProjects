import mysql.connector

con = mysql.connector.connect(
    host = "127.0.0.1",
    user = "root",
    password = "AdityaSQL2020",
    port = 3306,
    database = "AdityaDB"
)

cur = con.cursor()

sqlform = "Insert into employee1(Name,Salary) values(%s,%s)"

employees = [("harshit",20000),("Amit",30000),("Abhishek",45000),("Aditya",50000)]

cur.executemany(sqlform,employees)

con.commit()

cur.close()
con.close()