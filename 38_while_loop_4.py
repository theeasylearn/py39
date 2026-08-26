'''
write a program to findout factorial of given number
input : number 6 
process : 6 x 5 x 4 x 3 x 2  x 1 
output : 720 
'''
number = int(input("Enter number"))
if number == 1:
    factorial = 1
else:
    factorial = number - 1 #4
    factorial = factorial * number #20
    number = number - 2 #3

    while number>1: #condition
        #loop body 
        factorial = factorial * number #60
        number = number - 1 #2

print(factorial)


