mode = "r"
while True: 
    try:
        filename = input("Enter file name")
        #file open 
        file = open(filename,mode)
    except FileNotFoundError:
        print("File not found. please check files exist or not")
    except PermissionError:
        print("oops, you are trying to read folder. it is not possible")
    else:
        for line in file:
            print(line.strip())
        print("File read successfully")
        file.close()
        break 