'''
write a program to print following pattern 
        *
      *  *
    *  *  *
   *  *  *  * 
  *  *  *  *  *
'''
no_of_rows = int(input("Enter how many rows pyramid should have"))
for row in range(no_of_rows,1,-1): #outer loop
    for space in range(1,row-1): #inner loop for space 
        print('',end=' ')
    for astrik in range(0,(no_of_rows+1)-row): #inner loop for astrik 
        print(" *",end='')
    print("") #new line
