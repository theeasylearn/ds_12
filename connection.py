import mysql.connector as con
try:
    database = con.connect(host="localhost",user='root',passwd='',port=3306,database='ds12')
    print("Connection established....")
except con.Error as err:
    print("Error in Connection (read detail below)")
    print(err.errno)
    print(err.msg)

#create function
#function to run insert, update, delete 
def runSQL(sql,values=None):
    #create cursor
    mycursor = database.cursor()
    if values==None:
        mycursor.execute(sql)
    else:
        mycursor.execute(sql,values)
    return 1

#function to select statement
def fetchData(sql,values=None):
    mycursor = database.cursor()
    if values==None:
        mycursor.execute(sql)
    else:
        mycursor.execute(sql,values)
    return mycursor.fetchall()