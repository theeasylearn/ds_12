#multilevel inheritance 
class KB:
    #define constructor
    def __init__(self,bytes):
        #create instance variable bytes using input bytes 
        self.bytes = bytes 
    def getKB(self):
        #local variable 
        kilobytes = self.bytes / 1024
        return kilobytes
#INHERITANCE 
class MB(KB):
    def __init__(self, bytes):
        super().__init__(bytes) #calling parent class constrictor 
    def getMB(self):
        #create local variable
        temp = super().getKB()
        megabytes = temp / 1024
        return megabytes

class GB(MB):
    def __init__(self, bytes):
        super().__init__(bytes)
    def getGB(self):
        gigabytes = super().getMB() / 1024
        return gigabytes


bytes = int(input("Enter bytes "))
g1 = GB(bytes)
print("Giga bytes = ",round(g1.getGB(),2))





