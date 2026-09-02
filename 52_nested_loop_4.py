'''
write a program to print following pattern 
        *
      *  *
    *  *  *
   *  *  *  * 
  *  *  *  *  *
'''
for row in range(6,1,-1): #outer loop
    for space in range(1,row-1): #inner loop for space 
        print('',end=' ')
    for astrik in range(0,7-row): #inner loop for astrik 
        print(" *",end='')
    print("") #new line
