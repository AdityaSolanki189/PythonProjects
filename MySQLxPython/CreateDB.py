import mysql.connector

con = mysql.connector.connect(
    host = "127.0.0.1",
    user = "root",
    password = "AdityaSQL2020",
    port = 3306,
    database = "AdityaDB"
)

cur = con.cursor()

cur.execute("Create table employee1(Name varchar(200), Salary int(20))")


cur.close()

con.close()