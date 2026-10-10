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
            print("Press 1 to insert product")
            print("Press 2 to edit product")
            print("Press 3 to delete product")
            print("Press 4 to view product")
            print("Press 5 to search for product")
            print("Press 0 for exit")
            product_choice = int(input("Enter your choice"))
            if product_choice == 1:
                name = input("Enter Product Name")
                price = int(input("Enter product price"))
                quantity = int(input("Enter product quantity"))
                sql = "insert into product (name,price,quantity) values (%s,%s,%s)";
                values = [name,price,quantity]
                success = c.runSQL(sql,values)
                if success == 1:
                    print("Product added successfully")
                    key = input("Press any key to continue")
            elif product_choice == 2:
                print("let us edit product")
            elif product_choice == 3:
                print("let us delete product")
            elif product_choice == 4:
                sql = "select id,name,price,quantity from product order by name"
                products = c.fetchData(sql)
                for index,row in enumerate(products):
                    print(f"{row['id']:5} {'':5} {row['name']:<64} {row['price']:10} {row['quantity']:10}")
                    if (index+1)%10 == 0:
                        key = input("Press any key to continue")
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
