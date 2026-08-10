#dictionary related methods 
country = {'name':"India","ISD":91,"isAsia":True,"latitude":8.4}
print(country)
# country_2 = country #actually store reference of country into country_2 if update any one of two variable, it will update both 
country_2 = country.copy()
print(country_2)
country_2.clear() #remove all key value pair from country
print("country",country)
print("country 2",country_2)

print("Name ",country.get("name"))
print("Capital ",country.get("capital","not available"))
# print(country['capital'])
print("Dictionary values ",country.values())
print("Dictionary keys ",country.keys())
print("Dictionary key value as object ",country.items())

list = ['course','duration','fees']
print(list)
#create dictionary using list. value list will be the keys of dictionary
python = dict.fromkeys(list) 
print(python)
python['course'] = "Mastering python"
python['duration'] = 90
print(python)
country.pop("latitude",None)
print(country)
#remove last key value pair
country.popitem()
print(country)
country.update({'name':'bharat','capital':'delhi'})
print(country)
