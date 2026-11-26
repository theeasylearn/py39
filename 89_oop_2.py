#create class 
class Account:
    def setAccount(self):
        #self is used to create instance variable
        #instance variable variable which occupy separate memory space for each and every object 
        self.accountno = 1 
        self.balance = 9999 
        self.name = "shiv mehta" 
        self.gender = True  

    def display(self):
        #display all instance variable's value
        print("Account No ",self.accountno)
        print("Balance ",self.balance)
        print("Name ",self.name)
        print("Gender ",self.gender)
    
    def updateAccount(self,accno,nm,amount,gender):
        #if instance variable does not exist, it will create it 
        self.accountno = accno
        self.name = nm 
        self.balance = amount 
        self.gender = gender 

#create object
#objectname = ClassName()

a1 = Account()
a1.setAccount() #to create instance variable
a1.updateAccount(100,'Ankit Patel',1250000000,True) #update account detail
a1.display()

#create another object 
a2 = Account()
a2.setAccount() #compulsory to create instance variable 
a2.updateAccount(200,'Parth Joshi',123654789,True)
a2.display()

a3 = Account()
a3.setAccount()
accno = int(input("Enter account no"))
name = input("Enter Account holder name")
balance = int(input("Enter Balance"))
gender = input("Enter gender")

a3.updateAccount(accno,name,balance,gender)
a3.display()


