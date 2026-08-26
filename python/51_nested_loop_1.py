'''
write a program to print following pattern 
* 
* *
* * *
* * * *
* * * * *
'''
for row in range(1,6): #outer loop (5 times)
    for astrik in range(0,row): #(5 times)
        print("*",end='')
    print()
