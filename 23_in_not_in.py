#in and not in operator in python 
list = [10,20,30,40,50]
a = 10

isFound = a in list 
print(isFound)

isFound = a not in list 
print(isFound)

tuple = ("Ram","Krishna","Hanuman")
god = "Ram"

isFound = god in tuple
print(isFound)

isFound = god not in tuple 
print(isFound)

cities = "Bhavnagar Baroda Surat Ahmedabad rajkot"
city = "Baroda"

isFound = city in cities
print(isFound)

city = "Jamnagar"
isFound = city not in cities
print(isFound)