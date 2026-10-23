from datetime import datetime,timedelta

import project.connection as c 
def display_product():
    sql = "select id,name,price,quantity from product where is_deleted=0 order by name"
    products = c.fetchData(sql)
    print(f"{'id':<5} {'':<5} {'name':<70} {'price':10} {'quantity':10}")
    print("-"*100)
    GrandTotal = 0
    for index,row in enumerate(products):
        GrandTotal = GrandTotal + (row['price'] * row['quantity'])
        print(f"{row['id']:5} {'':5} {row['name']:<64} {row['price']:10} {row['quantity']:10}")
        if (index+1)%10 == 0:
            key = input("Press any key to continue")
    print("-"*110)
    print(f"Grand total = {GrandTotal}")
    
def display_bill_items():
    sql = "select i.id as id, productid,i.price,i.quantity,name from bill_item i,product p where productid=p.id and billid=0  order by i.id desc"
    table = c.fetchData(sql)
    if len(table)==0:
        print("There is no item in bill")
    else:
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
                sql = "SELECT sum(price*quantity) as 'amount' FROM `bill_item` where billid=0"
                bill_item = c.fetchData(sql)
                if len(bill_item)==0:
                    print("No item found in bill")
                else:
                    #display bill amount
                    amount = bill_item[0]['amount']
                    print(f"total bill amount = {amount}")
                    response = input("Are you sure to print bill (1 = yes/0 = no)")
                    if response=="1":

                        # accept bill detail such name,mobile,email from user 
                        name = input("Enter Customer Name")
                        mobile = input("Enter mobile no ")
                        email = input("Enter email address")

                        # insert new row into bill table 
                        sql = "insert into bill (name,mobile,email,amount) values (%s,%s,%s,%s)"
                        values = [name,mobile,email,amount]
                        success = c.runSQL(sql,values)
                        if success == 1:
                            print("Bill has been generated....")
                            #generate last bill id
                            
                            sql = "select max(id) as last_bill_id from bill"
                            bill = c.fetchData(sql)
                            bill_id = bill[0]['last_bill_id']
                            
                            # update bill_item set billid using last inserted row of bill table 
                            sql = "update bill_item set billid=%s where billid=0"
                            values = [bill_id]
                            success = c.runSQL(sql,values)
                              
                            #fetch productid and quantity of purchased items
                            sql = "select productid,quantity from bill_item where billid=%s"
                            values = [bill_id]
                            bill_item = c.fetchData(sql,values)
                            for row in bill_item:
                                productid = row['productid']
                                quantity = row['quantity']
                                sql = "update product set quantity=quantity - %s where id=%s"
                                values = [quantity,productid]
                                success = c.runSQL(sql,values)
                                if success==1:
                                   print("Bill has been successfully processed...")  
                            key = input("Press any key to continue")
                            # reduce stock of each and every item

                print('')
            elif bill_choice == 5:
                search_value = input("Enter customer name or bill date (%d-%m-%Y)")
                date = 0
                next_date = 0
                sql = ''
                try:
                    date = datetime.strptime(search_value, "%d-%m-%Y")
                    next_date = date + timedelta(days=1)
                    sql = "SELECT id,name,mobile,email,amount,date_format(created_at,'%d-%m-%Y') as bill_date FROM bill where created_at>=%s and created_at<%s"
                    values = [date,next_date]
                except ValueError as e:
                    print("invalid date")
                    sql = "SELECT id,name,mobile,email,amount,date_format(created_at,'%d-%m-%Y') as bill_date FROM bill where name like %s"
                    values = [f'%{search_value}%']
                print(sql)
                bill = c.fetchData(sql,values)
                if len(bill) == 0:
                    print("No bill found")
                else:
                    print(f"{'id':5} {'name':32} {'email':32} {'mobile':12} {'amount':10} {'bill_date':16}")
                    print("-"*100)
                    for row in bill:
                        print(f"{row['id']:5} {row['name']:32} {row['email']:32} {row['mobile']:12} {row['amount']:10} {row['bill_date']:16}")
                    key = input("Press any key to continue")
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
        while True:
            print("Press 1 for sales report between given dates")
            print("Press 2 for product stock reports ")
            print("Press 0 to return to main menu")
            choice = int(input("Enter your choice"))
            if choice == 1:
                shouldContinue = True
                while shouldContinue==True:
                    try:
                        start_date = input("Enter report start dates ")
                        end_date = input("Enter report end date")
                        start_date = datetime.strptime(start_date, "%d-%m-%Y")
                        end_date = datetime.strptime(end_date, "%d-%m-%Y")
                        sql = "SELECT id,name,mobile,email,amount,date_format(created_at,'%d-%m-%Y') as bill_date FROM bill where created_at>=%s and created_at<=%s"
                        values = [start_date,end_date]
                        bill = c.fetchData(sql,values)
                        if len(bill) == 0:
                            print("No bill found")
                        else:
                            print(f"{'id':5} {'name':32} {'email':32} {'mobile':12} {'amount':8} {'bill_date':16}")
                            print("-"*100)
                            GrantTotal = 0
                            count = 0
                            for row in bill:
                                print(f"{row['id']:5} {row['name']:32} {row['email']:32} {row['mobile']:12} {row['amount']:8} {row['bill_date']:16}")
                                GrantTotal = GrantTotal + row['amount']
                                count = count + 1
                            print("-"*110)
                            print(f"Total Bill = {count} Grand Total = {GrantTotal}")
                            print("-"*110)
                            key = input("Press any key to continue")
                        shouldContinue = False 
                    except ValueError as e:
                        print("invalid date")

            elif choice == 2:
               display_product()
            elif choice == 0:
                print("Return to main menu")
                break
            else:
                print("invalid choice")
        
    elif choice == 0:
        print("thank you for using our software, good bye")
        break #loop stop 
    else:
        print("not a valid choice")
