
school = {'name':'abc','year':1985,'class':12,'student':720}
print(school)

school2 = school.copy()
print(school,school2)

#empty school 2 
school2.clear()
print(school,school2)

#just get keys
print(school.keys())

print(school.values())

print(school.items())

print("school name",school.get("name"))
print("school name",school.get("email"))
print("school name",school.get("email",'email not found'))

school.pop('class')
school.popitem()
school.update({'name':'Bright school','city':'bhavnagar'})
print(school)

student = ['fullname','dob','gender','mobile','country']
print(student)

#create dictionary using list 
sarthak = dict.fromkeys(student)
sarthak['fullname']  = "sarthak shah"
print(sarthak)


