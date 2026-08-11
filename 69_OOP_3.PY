#Create class & class variables
class Student:
    #define class variable 
    srno = 1
    InstituteName = "The easylearn academy"
    #define constructor 
    def __init__(self,name,email):
        #create instance variable 
        self.name = name 
        self.email = email 
        self.rollno = Student.srno
        Student.srno+=1 
    def display(self):
        print("-"*100)
        print(self.rollno)
        print(self.name)
        print(self.email)
        print("-"*100)

#create object 
vatsal = Student("vatsal satiya","vatsal@gmail.com") #create 1st object
sarthak = Student("Sarthak shah","sarthak@gmail.com") #create 2nd object 

vatsal.display()
sarthak.display()
print(Student.InstituteName)
print(sarthak.InstituteName)
print(vatsal.InstituteName)
#change class variable's value using class 
Student.InstituteName = 'T.E.A'
print(Student.InstituteName)
print(sarthak.InstituteName)
print(vatsal.InstituteName)
