'''
write a program to findout given number is prime number or not
input : number 7 
output : prime number 

input : number 10
output : not prime number 

'''
number = int(input("Enter number"))
divisor = 2
if number == 2 or number%2==0:
    print("it is not prime number")
else:
    while divisor<number:
        reminder = number % divisor # 13 % 2 = 1
        if reminder == 0:
            print("it is not prime number")
            break #stop loop 
        divisor = divisor + 1 #3# 
    if divisor==number:
        print("it is prime number")