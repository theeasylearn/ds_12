def getMerit(maths,science,english,computer,history,drawing):
    print(maths,science,english,computer,history,drawing)
    total = maths + science + english
    return total 

m = int(input("Enter Maths marks: "))
s = int(input("Enter Science marks: "))
e = int(input("Enter English marks: "))
c = int(input("Enter Computer marks: "))
h = int(input("Enter History marks: "))
d = int(input("Enter Drawing marks: "))

# total = getMerit(c,h,d,m,s,e) #wrong way of calling function
total = getMerit(computer=c,history=h,drawing=d,maths=m,science=s,english=e) #proper way of calling function
print("merit ",total)

