'''
write a program to print following pattern 
1 0 1 0 1
1 0 1 0
1 0 1
1 0
1 
'''
row = 5
while row>=1:
    astrik = 1
    while astrik<=row:
        print(astrik%2,end='')
        astrik = astrik + 1
    print("") #new line
    row = row - 1