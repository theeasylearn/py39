from world.asia import countries as ai 
from world.europe import countries as eu 
from world.south_america import countries as sa 

#print all asian countries
print(ai.getCountries())
#print all europe countries
print(eu.getCountries())
#print all south_america countries
print(sa.getCountries())

#find is there any country India in asia 
print(ai.isCountryFound("India"))
print(ai.isCountryFound("Germany"))