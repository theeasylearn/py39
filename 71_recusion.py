# write a program to print following series 
# 2 4 6 8 10 12 ..... 100
#define function 
def printSeries(num):
    if num<=100:
        print(num,end=' ')
        num = num + 2 #4
        printSeries(num)
num = 2
printSeries(num)

