import connection as c 
while True: 
    print("Press 1 for Bill Management")
    print("Press 2 for Product Management")
    print("Press 3 for Reports ")
    print("Press 0 for Exit ")
    choice = int(input("Enter your choice"))
    if choice == 1:
        while True:
            print("-"*100)
            print("Bill Management")
            print("-"*100)
            print("Press 1 for Add items")
            print("Press 2 for delete items")
            print("Press 3 for view bill items")
            print("Press 4 for generate bill")
            print("Press 5 search for bill")
            print("Press 0 for exit")
            bill_choice = int(input("Enter bill choice"))
            if bill_choice == 1:
                print("let us add item into bill")
            elif bill_choice == 2:
                print("let us delete items from bill")
            elif bill_choice == 3:
                print("let us print all bill items")
            elif bill_choice == 4:
                print('let us generate bill')
            elif bill_choice == 5:
                print("let us search for bills")
            elif bill_choice == 0:
                print("let us return to main manu")
                break
            else:
                print("not valid choice")
    elif choice == 2:
        while True:
            print("-"*100)
            print("Product management")
            print("-"*100)
            print("Press 1 for Add Product")
            print("Press 2 for edit product")
            print("Press 3 for delete product")
            print("Press 4 for view product")
            print("Press 5 search for product")
            print("Press 0 for exit")
            product_choice = int(input("Enter your choice"))
            if product_choice == 1:
                print("let us add product")
            elif product_choice == 2:
                print("let us edit product")
            elif product_choice == 3:
                print("let us delete product")
            elif product_choice == 4:
                print("let us view all product")
            elif product_choice == 5:
                print("let us search product")
            elif product_choice == 0:
                print("let us exit to main menu")
                break
            else:
                print("not a valid choice ")
    elif choice == 3:
        print("let us develop reports")
    elif choice == 0:
        print("thank you for using our software, good bye")
        break #loop stop 
    else:
        print("not a valid choice")
