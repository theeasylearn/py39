#example of queue 
class Queue:
    def __init__(self):
        #create instance variable
        self.list = []
        self.front = -1
        self.rear = -1
        print("constructor called....")
    def enqueue(self,item):
        if self.front == -1:
            self.front = 0
        self.rear = self.rear + 1
        self.list.append(item) 
        
    def dequeue(self):
        if self.front == -1 or self.front > self.rear:
            print("Queue is empty")
        else:
            self.list[self.front] = None
            self.front = self.front + 1
            print("Item Removed")
    def display(self):  
        #local variable
        position = self.front
        if self.front==-1 or self.front > self.rear:
            print("Queue is empty")
        while position<=self.rear:
            print(f'{position} -> {self.list[position]}',end=' ')
            position+=1
        print('')
#create object
printer = Queue()
while True:
    print("Press 1 to enter new value into queue (Enqueue)")
    print("Press 2 to delete value from  queue (dequque)")
    print("Press 3 to display all values")
    print("Press 4 to exit")
    choice = int(input("Enter your choice"))
    if choice == 1:
        item = input("Enter value")
        printer.enqueue(item)
    elif choice==2:
        printer.dequeue()
    elif choice==3:
        printer.display()
    elif choice == 4:
        print("Good bye")
        break
    else:
        print("invalid choice")
