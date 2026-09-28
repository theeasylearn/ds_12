import mysql.connector as con
try:
    database = con.connect(host="localhost",user='root',passwd='',port=3306,database='ds12')
    print("Connection established....")
except con.Error as err:
    print("Error in Connection (read detail below)")
    print(err.errno)
    print(err.msg)
