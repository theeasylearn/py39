#create user defined function 
#with return value with argument function
def getSum(num1,num2,num3): #actual argument
    #local variable (only accessible inside function)
    sum = num1 + num2 + num3
    return sum 

def getMean(sum):
    #local variable 
    mean = sum / 3 
    return mean 

number1 = int(input("Enter 1st number"))
number2 = int(input("Enter 2nd number"))
number3 = int(input("Enter 3rd number"))

#calling/executing/using function 
result = getSum(number1,number2,number3) #formal argument
print(result)

mean = getMean(result) 
print(round(mean,2))
