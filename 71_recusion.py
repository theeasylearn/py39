def printNumber(number): #10
    if number<100:
        print(number) # 10
        number = number + 1 # 11
        printNumber(number) #call printNumber function from printNumber function
    print("last line of function",number)
number = 10 
printNumber(number)