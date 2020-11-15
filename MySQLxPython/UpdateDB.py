import mysql.connector

con = mysql.connector.connect(
    host = "127.0.0.1",
    user = "root",
    password = "AdityaSQL2020",
    port = 3306,
    database = "AdityaDB"
)

cur = con.cursor()

sql = "UPDATE employee1 SET Salary = 70000 WHERE Name = 'Amit'"
cur.execute(sql)

con.commit()
cur.close()
con.close()