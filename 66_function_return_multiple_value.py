def calculate(num1,num2):
    #create local variable 
    add = num1 + num2 
    sub = num1 - num2 
    mul = num1 * num2 
    div = num1 / num2 
    #function return multiple value as tuple (read only list)
    return add, sub, mul, div 


num1 = int(input("Enter 1st number"))
num2 = int(input("Enter 2nd number"))

result = calculate(num1,num2)

print("Result ")
print(result)
print("Addition ",result[0])
print("Subtraction ",result[1])
print("Multiplication ",result[2])
print("Division ",result[3])

#can copy value of tuple in different variables 
addition, subtraction, multiplication, division = calculate(num1,num2)
print("Addition ",addition)
print("Subtraction ",subtraction)
print("Multiplication ",multiplication)
print("Division ",division)