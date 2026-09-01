'''
write a program to print following pattern 
*
* *
* * *
* * * *
* * * * *
'''
for row in range(1,6): #outer loop
    for astrik in range(0,row): #inner loop 
        print("*",end=' ')
    print("")
