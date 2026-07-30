'''
write a program to print following pattern 
           *
         *  *     
       *  *  *     
     *  *  *  *     
   *  *  *  *  *     
'''
for row in range (5,0,-1):
    for space in range(1,row):
        print(" ",end='')
    for astrik in range(6,row,-1):
        print(" *",end='')
    
    print("") #new line
