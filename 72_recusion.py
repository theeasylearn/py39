# write a program to convert decimal number into binary number
# input : 8 output : 1000
def binary(number):
    if number>0:
        reminder = number % 2
        number = number // 2
        binary(number)
        print(reminder,end=' ')
number = int(input("Enter number"))
binary(number)



