import connection as c 

#create cursor 
mycursor = c.database.cursor()

#create sql statement
sql = "update users set name=%s,age=%s,weight=%s where id=%s"

# accept input 
name = input("Enter name")
age = int(input("Enter age"))
weight = float(input("Enter weight"))
id = int(input("Enter user id"))


#create list 
values = [name,age,weight,id]

#execute sql statement
mycursor.execute(sql,values)

#save changes
c.database.commit()

print(mycursor.rowcount, " rows has been updated successfully")

