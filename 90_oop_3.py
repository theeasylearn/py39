#create class 
class Account:
    #create constructor 
    def __init__(self,accountno,balance,name,gender):
        print("constructor called.....")
        #create instance variable
        self.accountno = accountno
        self.balance = balance
        self.name = name 
        self.gender = gender 

    def display(self):
        print("Account No ",self.accountno)
        print("Balance ",self.balance)
        print("Name ",self.name)
        print("Gender ",self.gender)
    def updateBalance(self,amount):
        self.balance = self.balance + amount
        print("balance updated successfully")
#create object
#objectname = ClassName()

a1 = Account(101,1250000,"Sahaj Patel",True) #it will call constructor automatically
a1.display()
# change balance 
a1.updateBalance(1111)
print("a1 user balance after balance is updated....")
a1.display()

accountno = int(input("Enter account No"))
name = input("Account holder name ")
balance = int(input("Enter balanace "))
gender = input("Enter gender ")

a2 = Account(accountno,balance,name,gender) #it will call constructor automatically
a2.display()
balance = int(input("Enter amount to update balance "))
a2.updateBalance(balance)
print("a2 user balance after balance is updated....")
a2.display()