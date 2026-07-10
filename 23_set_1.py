#create set 
fruits = {'apple','banana','mango','apple','pineapple'}
print(fruits)
fruits.add('kiwi')
fruits.add('cherry')
fruits.add('cherry')
fruits.remove('apple')
print(fruits)
numbers = [12, 45, 7, 23, 45, 89, 12, 56, 34, 78, 90, 23, 11, 67, 34, 5, 99, 56, 18, 45]
print(numbers)

unique_numbers = set(numbers) #set function remove duplicate numbers and return set
print(unique_numbers)
unique_numbers = list(unique_numbers)
print(unique_numbers)

#create 2 sets
set1 = {1,2,3,4,5}
set2 = {2,3,4,5,6}

union = set1.union(set2)
intersection = set1.intersection(set2)
difference = set1.difference(set2)

print("union ",union)
print("intersection ",intersection)
print("difference ",difference)
