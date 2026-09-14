# Without return value without argument
def printLine():
    print("-"*100)

# Without return value with argument
def printLetter(letter,times):
    print(letter*times)

# With return value without argument
def getPi():
    #here pi is local variable (we can use this variable only inside getPi function)
    pi = 22/7
    return pi 

printLine()
print("THE EASYLEARN ACADEMY")
printLine()
printLetter("*",50)
print("Python")
printLetter("~",75)

radius = int(input("Enter circle's radius"))
pi = getPi()
area = pi * radius * radius 
#round of digits upto 2 point
area = round(area,2)
print(f"Circle 's area = {area}")
