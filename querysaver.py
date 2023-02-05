from tkinter import *
import mysql.connector
conn = mysql.connector.connect(host='localhost', username='root', password='8318534234')
cr = conn.cursor()
print(conn)
cr.execute("show databases")
for i in cr:
    print(i)
conn.commit()
