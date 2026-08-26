#create dictionary
'''
    [] = list 
    {} = dictionary 
    () = tuple 
'''
book = {} #empty dictionary
print(book)

book['name'] = "atomic habit"
book['price'] = 1000
book['author'] = 'james clear'

print(book)

#add tuple into dictionary
book['chapters'] = (1,2,3,4)

#add list into dictionary
book['topics'] = ['abc','bcd','cde','def']

print(book)

# del book['chapters'][0]
# book['chapters'][0] = 100