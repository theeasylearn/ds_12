#write a program to calculate total score of team from given dictionary 
india = {
        "Rohit Sharma": 9,
        "Virat Kohli": 76,
        "Rishabh Pant": 0,
        "Suryakumar Yadav": 3,
        "Axar Patel": 47,
        "Shivam Dube": 27,
        "Hardik Pandya": 5,
        "Ravindra Jadeja": 2,
    }
total = 0
for player in india:
    # print(india[player]) #value of key
    total = total + india[player]
print(total)

#findout top score and scorer name 
#findout least score and scorer name 

