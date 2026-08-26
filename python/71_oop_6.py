#single level inheritance 
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
bytes = int(input("Enter bytes"))
#create object of KB class 
k = KB(bytes) #it will constructor __init__ and initialize instance variable bytes 
kilobytes = k.getKB()
print("KB = ",kilobytes)

m = MB(bytes) # it will call of MB constructor __init__ 
megabytes = m.getMB()
print("megabytes = ",round(megabytes,2))




