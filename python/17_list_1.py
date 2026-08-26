#example of list 
fruits = ['apple','banana','mango','pineapple','cherry','water melon','graps']
box = [1000,'car',12.7,True]
print(fruits)
#1st five item
print(fruits[0:5])
print(fruits[:3]) #first 3 fruit
print(fruits[3:]) #all the fruits from 3 position onwards

#display 1st fruit
print(fruits[0]) #apple

print(fruits[1]) #banana
print(box)
print(box * 2 )
print(fruits + box)

#add new item into list at the end
fruits.append('coconut')
fruits.append('kiwi')
print(fruits)

#add new item at start
fruits.insert(0,'custard apple')
print(fruits)

#remove apple (remove by name)
fruits.remove('apple')

#remove 1st value (by position)
fruits.pop(0)
print(fruits)