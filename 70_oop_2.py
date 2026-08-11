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

s1 = Student()
s1.whatICanDo()
s1.eat()
s1.walk()
s1.talk()
s1.read()
s1.write()
    