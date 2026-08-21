'''
write a program to accept week day number from user and display name of day.
input : 1 output : monday
input : 2 output : tuesday
'''
day = input("enter day of week")
#create dictionary 
week = {
    "1": "Monday",
    "2": "Tuesday",
    "3": "Wednesday",
    "4": "Thursday",
    "5": "Friday",
    "6": "Saturday",
    "7": "Sunday"
}
print(week.get(day,"not valid number"))