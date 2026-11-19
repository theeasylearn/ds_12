filename = "fruits.txt"
mode = "r"

#file open 
file = open(filename,mode)
for line in file:
    print(line.strip())

print("File read successfully")
file.close()