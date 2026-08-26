'''
write a program to print following pattern 
* * * * *
* * * *
* * *
* *
* 
'''
row = 5
while row>=1:
    astrik = 1
    while astrik<=row:
        print("*",end='')
        astrik = astrik + 1
    print("") #new line
    row = row - 1