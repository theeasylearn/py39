'''
write a program to accept week day number from user and display name of day.
input : 1 output : monday
input : 2 output : tuesday
'''
day = int(input("enter day of week"))
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("it is not valid day")

print("Good bye.")