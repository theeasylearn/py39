#write a program to findout gap between two dates 
from datetime import datetime as dt 
first_date = input("Enter earlier date (%d-%m-%Y)")
second_date = input("Enter later date (%d-%m-%Y)")
#convert into date object
first_date = dt.strptime(first_date,"%d-%m-%Y")
second_date = dt.strptime(second_date,"%d-%m-%Y")
difference = second_date - first_date
print("difference = ",difference)
print("difference in year = ",round(difference.days/365,0))
