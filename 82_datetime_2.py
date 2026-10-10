#convert string date into date object
from datetime import datetime as dt 
birth_date = input("Enter birth date (%d-%m-%Y)")
print("BIRTH DATE = ",birth_date)

#convert it into date 
birth_date = dt.strptime(birth_date,'%d-%m-%Y')

print(birth_date)