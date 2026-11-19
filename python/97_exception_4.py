mode = "r"
while True: 
    try:
        filename = input("Enter file name")
        #file open 
        file = open(filename,mode)
    except (FileNotFoundError,PermissionError):
        print("Either file does not exist or it is not file. perhaps it is directory")
    else:
        for line in file:
            print(line.strip())
        print("File read successfully")
        file.close()
        break 