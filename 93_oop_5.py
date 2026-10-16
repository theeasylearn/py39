#create class 
class Stack:
    #class variable
    size = 5
    def __init__(self):
        #create instance variable 
        self.list = [] #create empty list 
        self.top = -1 #stack is empty 
        print("Constructor called.....")
    def push(self,value):
        if self.top == Stack.size - 1:
            print("Stack overflow (stack is full)")
        else:
            self.top = self.top + 1
            self.list.append(value)
            print("value is added at the top")
            
    def display(self):
        if self.top == -1:
            print("stack is empty")
        else:
            print("value in stack")
            for item in reversed(self.list):
                print(item)
    def pop(self):
        print("pop method called...")
        if self.top == -1:
            print("Stack underflow (stack is empty)")
        else:
            print(self.list[self.top], " value removed")
            del self.list[self.top]
            self.top  = self.top - 1

#create object
s1 = Stack() #it will call constructor 

while True:
    print("Press 1 to push item into stack")
    print("Press 2 to pop item from stack")
    print("Press 3 display stack")
    print("Press 4 to exit")
    choice = int(input("Enter choice"))
    if choice == 1:
        value = input("Enter value to push into stack")
        s1.push(value)
    elif choice == 2:
        s1.pop()
    elif choice == 3:
        s1.display()
    elif choice == 4:
        print("Good bye")
        break #loop break(stop)
    else:
        print("invalid choice")