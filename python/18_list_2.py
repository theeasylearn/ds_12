# list related functions
vegetables = ["Potato", "Tomato", "Onion", "Brinjal", "Potato","Lady Finger", "Cabbage", "Cauliflower", "Carrot", "Radish", "Beetroot", "Spinach", "Fenugreek", "Coriander","Potato", "Mint", "Green Peas", "Capsicum", "Bottle Gourd", "Ridge Gourd", "Sponge Gourd", "Bitter Gourd", "Snake Gourd", "Ash Gourd", "Pumpkin", "Cucumber", "Zucchini", "Drumstick","Potato", "Raw Banana", "Elephant Foot Yam", "Sweet Potato", "Taro Root", "Turnip", "French Beans", "Cluster Beans", "Broad Beans", "Cowpea Beans", "Green Chilli", "Red Chilli", "Garlic", "Ginger", "Spring Onion", "Celery", "Lettuce", "Broccoli", "Mushroom", "Corn", "Raw Papaya", "Raw Mango", "Curry Leaves", "Amaranth Leaves", "Mustard Greens", "Dill Leaves", "Colocasia Leaves", "Ivy Gourd", "Pointed Gourd", "Kohlrabi", "Leek", "Fennel", "Parsley", "Artichoke", "Asparagus", "Bok Choy", "Cherry Tomato", "White Pumpkin", "Lotus Stem", "Jackfruit", "Rhubarb", "Water Spinach", "Moringa Leaves", "Chayote", "Yardlong Beans", "Turmeric Root", "Purple Cabbage", "Red Onion", "Shallots", "Baby Corn", "Green Garlic", "Sorrel Leaves", "Malabar Spinach", "Arbi", "Kachri"]

fruits = ["Apple", "Banana", "Mango", "Orange", "Grapes", "Pineapple", "Papaya", "Guava", "Watermelon", "Muskmelon", "Pomegranate", "Kiwi", "Strawberry", "Blueberry", "Blackberry", "Raspberry", "Cherry", "Peach", "Pear", "Plum", "Apricot", "Litchi", "Custard Apple", "Sapota", "Jackfruit", "Coconut", "Fig", "Dates", "Dragon Fruit", "Passion Fruit", "Avocado", "Star Fruit", "Mulberry", "Jamun", "Indian Gooseberry", "Wood Apple", "Bael", "Tamarind", "Lemon", "Sweet Lime", "Mandarin", "Cranberry", "Gooseberry", "Persimmon", "Pomelo", "Durian", "Mangosteen", "Longan", "Rambutan", "Olives", "Black Currant", "Red Currant", "Breadfruit", "Rose Apple", "Wax Apple", "Soursop", "Hog Plum", "Velvet Apple", "Miracle Fruit", "Karonda", "Phalsa", "Kokum", "Bilimbi", "Monstera Fruit", "Nance", "Quince", "Salak", "Ugli Fruit", "Cempedak", "Langsat", "Loquat", "Medlar", "Jujube", "Noni", "Santol", "Sugar Apple", "Surinam Cherry", "Tangerine", "White Sapote", "Yuzu", "Cloudberry"]

print(vegetables) 
print(fruits)
# print(vegetables+fruits) #temporary 
# or 
vegetables.extend(fruits) #join permanent 
print(vegetables)

fruits.clear() #remove all items from fruits. fruits become empty 
print(fruits)

position = vegetables.index("Cabbage") #index return position of Cabbage
print("position of Cabbage ",position)
# position = vegetables.index("abc") #index return position of abc
# print("position of abc ",position)

#count Potato
count = vegetables.count("Potato")
print("count of Potato",count)

#count abc
count = vegetables.count("abc")
print("count of abc",count)


#sorting
vegetables.sort()
print("vegetables = ",vegetables)

#reverse list 
vegetables.reverse()
print(vegetables)

# wrong way of copying list 
# vegetables2 = vegetables # = operator store reference of vegetables into vegetables

#right way of copying list 
vegetables2 = vegetables.copy() 
vegetables2.clear() 
print(vegetables)