class Currency:
    #constructor
    def __init__(self,rupees):
        #create instance variable
        self.rupees = rupees
    def getDollar(self):
        result = self.rupees / 91
        return result 
    def getEuro(self):
        result = self.rupees / 100
        return result 
    def getPound(self):
        result = self.rupees / 110
        return result 

rupees = int(input("Enter rupees"))
c1 = Currency(rupees)

print("Dollar = ",c1.getDollar())
print("Euro = ",c1.getEuro())
print("Pound = ",c1.getPound())
