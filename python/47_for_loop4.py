#write a program to findout how many vowels are their in given sentence 
sentence = "apple banana"
vowel = 0
for letter in sentence:
    #print(letter,end=' ')
    if letter == 'a' or letter == 'e' or letter =='i' or letter == 'o' or letter =='u':
        vowel+=1

print("vowels = ",vowel)