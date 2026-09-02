'''
write a program to print following pattern 
      1
     0 1
    0 1 0
   1 0 1 0
  1 0 1 0 1     
'''
no_of_rows = int(input("Enter how many rows pyramid should have"))
num = 1
for row in range(no_of_rows,1,-1): #outer loop
    for space in range(1,row-1): #inner loop for space 
        print('',end=' ')
    for astrik in range(0,(no_of_rows+1)-row): #inner loop for astrik 
        print(f" {num}",end='')
        if num == 1:
            num = 0
        else:
            num = 1
    print("") #new line
