#assume you are in mall, you are required to decide which toothpaste you should buy based upon price of toothpaste. you want to buy cheaper toothpaste. how will you do that 
# 1st toothpaste weight = 100gram price 200 rs  2 rs per gram 
# 2nd toothpaste weight = 200gram price 300 rs  1.5rs per gram 

print("Enter 1st toothpaste detail")
price_1 = int(input("Enter 1st tooth paste price"))
weight_1 = int(input("Enter 1st tooth paste weight in grams"))

print("Enter 2nd toothpaste detail")
price_2 = int(input("Enter 2nd tooth paste price"))
weight_2 = int(input("Enter 2nd tooth paste weight in grams"))

price_per_gram_1 = price_1 / weight_1
price_per_gram_2 = price_1 / weight_2 

print("tooth paste 1 price per gram ",price_per_gram_1)
print("tooth paste 2 price per gram ",price_per_gram_2)


if price_per_gram_1<price_per_gram_2:
    print("tooth paste 1 in cheaper then tooth paste 2")
else:
    print("tooth paste 2 is cheaper then tooth paste 1")

print("Good bye.")


