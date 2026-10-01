import connection as c 

#create cursor 
mycursor = c.database.cursor(dictionary=True)

#create sql statement
sql = "select * from users order by id desc"

#execute sql statement
mycursor.execute(sql)

#fetch 1 row
# row = mycursor.fetchone()
# print(row) #dictionary

tables = mycursor.fetchall() #return list of dictionary
# print(tables)
print(f"{'id':<10} {'name':<48} {'age':<12} weight")
print("-"*100)
count = 0
for row in tables:
    msg = f"{row['id']:<10} {row['name']:<48} {row['age']:<12} {row['weight']}"
    print(msg)
    count=count+1
    if count%10==0:
        key = input("Press any key to continue")
print(f"{count } records found")