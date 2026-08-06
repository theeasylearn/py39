#example of list related methods
fruits = ['mango','pineapple','orange','kiwi','apple','banana','watermelon','graps','banana']
vegetable = ['Potato','Tomato','lady finger']
print(fruits)
fruits.extend(vegetable) #merge fruits and vegetable
print(fruits)
fruits.remove('Potato')
fruits.remove("Tomato")
# fruits.remove("Onion")
fruits.pop(1)
print(fruits)
vegetable.clear()
print(vegetable)
print("Position of mango " ,fruits.index("mango"))
print("Position of kiwi " ,fruits.index("kiwi"))
# print("Position of garlic " ,fruits.index("garlic"))
print("Count of banana ",fruits.count("banana"))
fruits.sort()
print("after sort fruit = ",fruits)
fruits.reverse()
print("after reverse fruits = ",fruits)

#create copy of fruits 
fruits_2 = fruits.copy() #shallow copy of list
print(fruits_2)
fruits_2.clear()
print(fruits,fruits_2)
print("no of item in fruits ",len(fruits))