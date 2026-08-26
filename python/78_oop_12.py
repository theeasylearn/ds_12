# //multilevel inheritance
class Human:
    def walk(self):
        print("I can walk")
    def talk(self):
        print("I can talk")
    def eat(self):
        print("I can eat")

#Student class inheri/extends Human
class Student(Human):
    def read(self):
        print("I can read")
    def write(self):
        print("I can write")
    def whatICanDo(self):
        #calling parent class method 
        super().eat()
        super().walk()
        super().talk()
        #calling own class method 
        self.read()
        self.write()
class Teacher(Student):
    def teach(self):
        print("I can teach")
    def doughs(self):
        print("I can help to solve doughs")
    def whatICanDo(self):
        super().whatICanDo()
        self.teach()
        self.doughs()
class Developer(Student):
    def code(self):
        print("I can write code in python")
    def debug(self):
        print("I can debug python code")
    #method overidding 
    def whatICanDo(self):
        super().whatICanDo()
        self.code()
        self.debug()

#create object of developer class 
d1 = Developer() 
d1.whatICanDo() #calling whatICanDo method of Developer 

t1 = Teacher()
t1.whatICanDo()