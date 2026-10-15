#create class 
class Stack:
    def __init__(self):
        #create instance variable 
        self.list = [] #create empty list 
        self.top = -1 #stack is empty 
        print("Constructor called.....")
    def push(self,value):
        self.top = self.top + 1
        self.list.append(value)
        print("value is added at the top")
    def display(self):
        print("value in stack")
        for item in reversed(self.list):
            print(item)
    def pop(self):
        print("pop method called...")
        print(self.list[self.top], " value removed")
        del self.list[self.top]
        self.top  = self.top - 1

#create object
s1 = Stack() #it will call constructor 
#stack add 5 values 
s1.push(10)
s1.push(20)
s1.push(100)
s1.push(200)
s1.push(300)
s1.display()
s1.pop()
s1.pop()
s1.display()