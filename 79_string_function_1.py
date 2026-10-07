name = "The Easylearn Academy"
print(name)
print(name.upper())
print(name.lower())

city = "bhavnagar"
pincode = "364001"
username = "ankit3385"
temp = " "
print("City ",city)
print("Pincode ",pincode)
print("Username ",pincode)
print("Temp ",temp)
print(f"{city} is in lower case",city.islower())
print(f"{city} is in lower case",city.isupper())
print(f"{pincode} has only numbers ",pincode.isnumeric())
print(f"{pincode} has only alphabets ",pincode.isalpha())
print(f"{city} has only alphabets ",city.isalpha())
print(f"{username} has only alphabets + numbers ",username.isalnum())
print(f"{name} is in title case ",name.istitle())
print(f"{temp} has only space ",temp.isspace())
print(f"length of {name} ",len(name))
print(f"length of {pincode} ",len(pincode))

countries = ['Switzerland','Norway','Brazil','japan','newzland']
connector = " "
print(connector.join(countries))
gods = ("Shiv","Vishnu","Brama")

print(connector.join(gods))

dish = "Undhiyu Sev_Tameta_Nu_Shaak Ringan_No_Olo Bhinda_Sambhariya " \
    + "Tindora_Nu_Shaak Dudhi_Chana_Nu_Shaak Bataka_Nu_Shaak Guvar_Dhokli_Nu_Shaak " \
    + "Karela_Nu_Shaak Ganthiya_Nu_Shaak Kaju_Gathiya Papdi_Muthiya_Nu_Shaak " \
    + "Methi_Papad_Nu_Shaak Ravaiya Fansi_Dhodha_Nu_Shaak Lasaniya_Batata" 
print(dish)
print(dish.split())

line = "I have bike, i use bike to go office"
print(line)
print(line.replace("bike","car"))
print(line.replace("bike","car",1))