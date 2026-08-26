#write a program to findout lucky number for user from his/her birthdate
#birthdate : 12 -> process 1+2 output 3 
#birthdate : 19 -> process 1+9 output 10
#birthdate : 25 -> process 2+5 output 7

day = int(input("enter your birth date (only day not month & year)")) #12
last = day % 10  #2 
first = day // 10 #1
lucky_number = first + last 
print("your lucky number is ",lucky_number)
# print(first,last)