# multiple inheritance 
class Human:
    def walk(self):
        print("I can walk")
    def talk(self):
        print("I can talk")
    def eat(self):
        print("I can eat")
class Robo:
    def cleaning(self):
        print("I can do cleaning")
    def lifting(self):
        print("I can lift weight")

class Cyborg(Human,Robo):
    def repeat(self):
        print("I can do same task many times without rest and boredem")
    def whatICanDo(self):
        super().walk()
        super().talk()
        super().eat()
        super().cleaning()
        super().lifting()

c1 = Cyborg()
c1.whatICanDo()