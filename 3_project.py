import connection as c 
def display_product():
    sql = "select id,name,price,quantity from product where is_deleted=0 order by name"
    products = c.fetchData(sql)
    print(f"{'id':<5} {'':<5} {'name':<70} {'price':10} {'quantity':10}")
    print("-"*100)
    for index,row in enumerate(products):
        print(f"{row['id']:5} {'':5} {row['name']:<64} {row['price']:10} {row['quantity']:10}")
        if (index+1)%10 == 0:
            key = input("Press any key to continue")
def display_bill_items():
    sql = "select i.id as id, productid,i.price,i.quantity,name from bill_item i,product p where productid=p.id and billid=0  order by i.id desc"
    table = c.fetchData(sql)
    print(f"{'itemID':<8}{'id':4} {'name':<62} {'price':<10} {'quantity':<10} {'total' :<10}")
    print("-"*110)
    bill_total = 0
    item_count = 0
    for row in table:
        print(f"{row['id']:8} {row['productid']:4} {row['name']:<62} {row['price']:<10} {row['quantity']:<10} {row['price'] * row['quantity'] :<10}")
        item_count = item_count + row['quantity']
        bill_total = bill_total + (row['price'] * row['quantity'])

    print("-"*110)
    print(f"Total Item = {item_count} Total Bill Amount = {bill_total}")
    print("-"*110)
    key = input("Press any to continue")
while True: 
    print("Press 1 for Bill Management")
    print("Press 2 for Product Management")
    print("Press 3 for Reports ")
    print("Press 0 for Exit ")
    choice = int(input("Enter your choice"))
    if choice == 1:
        #fetch all product id and their price as key value pair 
        sql = "select id,price from product where is_deleted=0 order by id "
        products = c.fetchData(sql)
        product_list = [] #empty list 
        for row in products:
            temp = {row['id']:row['price']}
            product_list.append(temp)
        # print(product_list)
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
                #display all products 
                display_product()
                #accept productid 
                id = int(input("Enter product id "))
                #check productid is valid or invalid
                if not any(id in product_id for product_id in product_list):
                    print("Product not found")    
                else:
                    #if valid productid then we accept quantity from users
                    quantity = int(input("Enter purchase count(no of pcs)"))
                    #run sql statement to insert row into bill item table 
                    sql = "insert into bill_item (productid,quantity,price,billid) values (%s,%s,%s,%s)"
                    price = next((item[id] for item in product_list if id in item), None)
                    values = [id,quantity,price,0]
                    success = c.runSQL(sql,values)
                    if success == 1:
                        print("Item added into bill")
                key = input("Press any key to continue")
            elif bill_choice == 2:
                #display all items in bill 
                display_bill_items()
                #accept item id from user 
                item_id = int(input("Enter Item id"))
                # check item id exists or not 
                sql = "select productid from bill_item where id=%s"
                values = [item_id]
                bill_item = c.fetchData(sql,values)
                if len(bill_item)==0:
                    print("ITEM ID not found in bill")
                else:
                    # if item id found then we run delete sql statement    
                    sql = "delete from bill_item where id=%s"
                    values = [item_id]
                    success = c.runSQL(sql,values)
                    if success == 1:
                        print("item has been deleted from bill")
                key = input("Press any key to continue")

            elif bill_choice == 3:
                display_bill_items()
            elif bill_choice == 4:
                # calculate bill amount
                # accept bill detail such name,mobile,email from user 
                # insert new row into bill table 
                # update bill_item set billid using last inserted row of bill table 
                # reduce stock of each and every item
                print('')
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
                # display all products
                display_product()
                # accept id of product to be updated 
                id = int(input("enter product id to update product"))
                # check whether id exists or not 
                sql = "select id from product where id = %s"
                values = [id]
                products = c.fetchData(sql,values) #list of dictionary
                if len(products)==0:
                    print("No product found")
                else:
                    # if id found, accept name, price, quantity from user 
                    name = input("Enter Product Name")
                    price = int(input("Enter product price"))
                    quantity = int(input("Enter product quantity"))
                    # run update sql statement
                    sql = "update product set name=%s,price=%s,quantity=%s where id=%s"
                    values = [name,price,quantity,id]
                    success = c.runSQL(sql,values)
                    if success == 1:
                        print("product updated successfully")
                key = input("Press any key to continue")
            elif product_choice == 3:
                print("let us delete product")
                #display all products 
                display_product()
                id = int(input("enter product id to delete product"))
                sql = "update product set is_deleted=1 where id=%s"
                values = [id]
                success = c.runSQL(sql,values)
                if success == 1:
                    print("product has been deleted")
            elif product_choice == 4:
                display_product()
            elif product_choice == 5:
                search_value = input("Enter product name")
                sql ="select id, name, price, quantity from product where name like %s and is_deleted=0 order by name"
                values = [f'%{search_value}%']
                products = c.fetchData(sql,values)
                #print(products) #list of dictionary 
                print(f"{'id':<5} {'':<5} {'name':<70} {'price':10} {'quantity':10}")
                print("-"*100)
                if len(products)==0:
                    print("No Product found")
                else:
                    for row in products:
                        print(f"{row['id']:5} {'':5} {row['name']:<64} {row['price']:10} {row['quantity']:10}")
                key = input("Press any key to continue")
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
