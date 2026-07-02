'''
write a program to generate de-nomination of given amount in indian currency 
input: 886 
 500 x 1 = 500
 200 x 1 = 200
 100 x 1 = 100
 50 x 1 =   50
 20 x 1 =   20
 10 x 1 =   10
 5 x 1 =    05
 1 x 1 =    0
'''
amount = int(input("Enter amount")) 
five_hd = amount // 500
amount = amount - (five_hd * 500) 

two_hd = amount // 200
amount = amount - (two_hd * 200) 

one_hd = amount // 100
amount = amount - (one_hd * 100) 

fifty = amount // 50
amount = amount - (fifty * 50) 

twenty = amount // 20
amount = amount - (twenty * 20) 

ten = amount // 10
amount = amount - (ten * 10) 

five = amount // 5
amount = amount - (five * 5) 

two = amount // 2
amount = amount - (two * 2) 

one = amount // 1
amount = amount - (one * 1) 

print(f"Five hundred = {five_hd}")
print(f"two hundred = {two_hd}")
print(f"one hundred = {one_hd}")
print(f"Fifty = {fifty}")
print(f"twenty = {twenty}")
print(f"ten = {ten}")
print(f"five = {five}")
print(f"two = {two}")
print(f"one = {one}")