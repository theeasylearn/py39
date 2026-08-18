'''
    write a program to findout how many days in given month. 
    input : 1 output : this month has 31 days 
    input : 2 output : this month has 28/29 days 
    input : 4 output : this month has 30 days 

    31 days : 1, 3, 5, 7,8, 10, 12
    30 day : 4,6,9,11
    28/29 days :  2
'''
month = int(input("Enter month between 1 to 12"))
if month == 2:
    print("this month has 28/29 days")
    exit() #stop python code 
if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    print("this month has 31 days")
else:
    print("this month has 30 days")




