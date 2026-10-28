import os 
while True:
    print("Press 1 to create new directory")
    print("Press 2 to change current directory")
    print("Press 3 to get current directory")
    print("Press 4 to delete particular directory")
    print("Press 0 to exit")
    choice = int(input("Enter your choice"))
    if choice == 1:
        name = input("Enter new directory name")
        os.mkdir(name)
    elif choice == 2:
        name = input("Enter directory name to set as active directory")
        os.chdir(name)
    elif choice == 3:
        print(os.getcwd())
    elif choice == 4:
        name = input("Enter directory name to delete")
        os.rmdir(name)
    elif choice == 0:
        print("Good bye")
        break
    else: 
        print("invalid choice")
