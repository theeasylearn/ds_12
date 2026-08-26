# multiple inheritance 
class Farm:
    def __init__(self,length,width):
        self.length = length 
        self.width = width 
    def getValue(self):
        #return total valuation of Farm 
        return self.length * self.width * 10000
class Gold:
     def __init__(self,grams):
            self.grams = grams 
     def getValue(self):
            return self.grams * 150000

class Property(Farm,Gold):
     def __init__(self, length, width,gram):
          Farm.__init__(self,length, width)
          Gold.__init__(self,gram)
     def getTotalValue(self):
          return Farm.getValue(self) + Gold.getValue(self)

p1 = Property(100,200,5)
print(p1.getTotalValue())
        