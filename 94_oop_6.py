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
        if self.front == -1:
            print("Queue is empty")
        else:
            self.list[self.front] = None
            self.front = self.front + 1
            print("Item Removed")
    def display(self):  
        #local variable
        position = self.front
        while position<=self.rear:
            print(f'{position} -> {self.list[position]}',end=' ')
            position+=1
        print('')
#create object
printer = Queue()
printer.enqueue('Office Document')
printer.enqueue("Powerpoint presentation")
printer.enqueue("Excel spread sheet")
printer.enqueue("Photo")
printer.display()
printer.dequeue()
printer.dequeue()
printer.display()
