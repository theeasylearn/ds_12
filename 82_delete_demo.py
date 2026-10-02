import connection as c #c is alias (nickname)
#create cursor 
mycursor = c.database.cursor()

#sql statement 
sql = "delete from users where id=%s" #%s placeholder
userid = int(input("Enter user id"))
values = [userid]

#execute sql statement 
mycursor.execute(sql,values)

#commit changes 
c.database.commit()

#print how many rows has been affected 
print(mycursor.rowcount, "rows has been deleted")