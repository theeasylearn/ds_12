'''
write a program to generate de-nomination of given amount in indian currency 
assume person amit wants to give 886 rupees to meena without accept any changes. amit will given this amount using biggest possible currency note. 

input: 888 
 500 x 1 = 500
 200 x 1 = 200
 100 x 1 = 100
 50 x 1 =   50
 20 x 1 =   20
 10 x 1 =   10
 5 x 1 =    05
 2 x 1 =    02
 1 x 1 =    01
'''

#assume amount is 888
amount = int(input("Enter amount"))
five_hundred = amount // 500
amount = amount - (five_hundred * 500)
two_hundred = amount // 200
amount = amount - (two_hundred * 200)
one_hundred = amount // 100
amount = amount - (one_hundred * 100)
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

print("500 X ",five_hundred)
print("200 X ",two_hundred)
print("100 X ",one_hundred)
print("50 X ",fifty)
print("20 X ",twenty)
print("10 X ",ten)
print("5 X ",five)
print("2 X ",two)
print("1 X ",one)
