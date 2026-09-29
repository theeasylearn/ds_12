import connection as c 

#create cursor 
mycursor = c.database.cursor(dictionary=True)

#create sql statement
sql = "select * from users order by id desc"

#execute sql statement
mycursor.execute(sql)

#fetch 1 row
# row = mycursor.fetchone()
# print(row)

tables = mycursor.fetchall()
print(tables)

