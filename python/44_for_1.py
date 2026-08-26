# write a program to calculate and display sum & average of all the values in list
numbers = [12, 45, 7, 89, 23, 56, 91, 34, 18, 67, 5, 72, 39, 84, 26, 11, 95, 48, 63, 30,100]
sum = 0
count = 0
for num in numbers:
    # print(num)
    sum = sum + num
    count = count + 1

average = sum / count
print(f"sum = {sum} no of items = {count} average = {average:.2f}")