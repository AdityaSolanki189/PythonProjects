import mysql.connector

#connecting to the database
con = mysql.connector.connect(
    host = "127.0.0.1",
    user = "root",
    password = "AdityaSQL2020",
    port = 3306
)

print(con)

if(con):
    print("Connection Successful!")
else:
    print("Connection UnSuccessful!")

#cursor
mycursor = con.cursor()
#execute the query
mycursor.execute("Show Databases")
for db in mycursor:
    print(db)
#close cursor
mycursor.close()

#close the connection
con.close()