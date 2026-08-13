# Hierarchical inheritance 
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
class Actor(Human):
        def Acting(self):
            print("I can do acting")
        def Dancing(self):
            print("I can do dancing")
        def Fighting(self):
            print("I can do fighting")
        def whatICanDo(self):
            #calling parent class method 
            super().eat()
            super().walk()
            super().talk()
            self.Acting()
            self.Dancing()
            self.Fighting()

s1 = Student()
s1.whatICanDo()
s1.eat()
s1.walk()
s1.talk()
s1.read()
s1.write()
print("-"*120)
a1 = Actor()
a1.whatICanDo()
a1.Acting()
a1.Dancing()
a1.Fighting()

    