south_american_countries = ["Argentina", "Bolivia", "Brazil", "Chile", "Colombia", "Ecuador", "Guyana", "Paraguay", "Peru", "Suriname", "Uruguay", "Venezuela"]
def getCountries():
    global south_american_countries
    return south_american_countries 
def isCountryFound(country): #France
    global south_american_countries
    if country in south_american_countries:
        return True
    else: 
        return False


