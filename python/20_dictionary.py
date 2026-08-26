# create dictionary
teacher = {'name':'ankit','age':42,'weight':81.25,'gender':True}
print(teacher)

#update key value pair
teacher['name'] = "Ankit Patel"

#insert new key value pair 
teacher['email'] = 'ankit3385@gmail.com'

print(teacher)

#accessing specific key
print(teacher['age'])

#delete key value pair
del teacher['email']

print(teacher)

#delete whole dictionary
# del teacher
# print(teacher)