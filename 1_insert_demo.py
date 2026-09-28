import connection as c #c is alias (nick name)
mycursor = c.database.cursor()
sql = "insert into users (name,age,weight) values (%s,%s,%s)"
name = input("What is your name")
age = int(input("what is your age"))
weight = float(input("what is your weight"))
values = [name,age,weight]
mycursor.execute(sql,values)
c.database.commit()
print(mycursor.rowcount, "row inserted....")

