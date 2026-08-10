#example of dictionary 
'''
    [] brackets used to create list 
    () parenthesis used to create tuples 
    {} braces  used to create dictionary 
    <> angel brackets 
'''
book = {} #empty dictionary
print(book)
#add key value pair 
book['name'] = "Learning Python"
book['price'] = 500
book['author'] = "Ankit Patel"
print(book)
book['price'] = 599
print(book['price'])
#add list into dictionary
book['topics'] = ['Index','introduction','variables','control statements','functions']
print(book)
#add tuples into dictionary 
book['chapters'] = (1,2,3,4,5)
print(book)
#accessing particular element inside list (introduction)
print(book['topics'][1])
#accessing particular element inside tuple (3)
print(book['chapters'][2])
#update particular element inside list (introduction)
book['topics'][1] = "introduction to python"
print(book['topics'][1])

# book['chapters'][1] = 5
del book['chapters'][1]