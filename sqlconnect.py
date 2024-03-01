import mysql.connector

conn = mysql.connector.connect(host = "localhost",database = " APIDevelop", user = "root",password = "j@a#na21G")

cursor = conn.cursor()

print(conn.is_connected())

mysql = "SELECT * FROM CustomerInfo"
cursor.execute(mysql)
rows = cursor.fetchall()
print(rows)


