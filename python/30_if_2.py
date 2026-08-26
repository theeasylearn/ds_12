#write a findout & display profit or loss amount  from given purchase & sales price of the product
purchase_price = float(input("Enter product purchase price"))
sales_price = float(input("Enter sales price"))

difference = sales_price - purchase_price

if difference>0:
    print("you have made profit of ",difference)

if difference<0:
    print("you have made loss of ",difference)

if difference==0:
    print("you have made no profit no loss")

print("Good bye")

