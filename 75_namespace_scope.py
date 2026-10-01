balance = 10000
def addMoney(amount):
    global balance #this line is required to access global variable balance 
    # balance = 0 #here balance local variable
    balance = balance + amount 
    print("Balance should be updated....")

print(f"before running AddMoney {balance}")
addMoney(1234)
print(f"after updating AddMoney {balance}")


