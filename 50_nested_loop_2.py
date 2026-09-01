'''
write a program to print following pattern 
1 2 3 4 5
1 2 3 4
1 2 3
1 2 
1
'''
row = 5
while row>=1:
    number = 1
    while number<=row: #inner loop 1<=1
        print(number,end=' ')
        number = number + 1
    print("")
    row = row - 1
