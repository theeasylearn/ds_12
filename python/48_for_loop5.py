#write a program to findout how many vowels are their in given sentence 
sentence = "apple banana"
vowel = 0
list = ['a','e','i','o','u']
for letter in sentence:
    if letter in list:
        vowel+=1
print("vowels = ",vowel)