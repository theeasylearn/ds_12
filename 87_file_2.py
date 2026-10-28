filename = "fruits.txt"
mode = "r"

#file open 
file = open(filename,mode)
content = file.read() #reads entire file and store it's content into content variable
print(content) #print content variable 
print("File read successfully")
file.close()
