# write a program to display following series 
# 0 1 1 2 3 5 8 13 21 34 ...... 100
#       p c n
number = 1  

previous = 0 
current = 1
next = previous + current
print(previous,end=' ')
print(current,end=' ')

while next<100:
    print(next,end=' ')
    previous = current
    current = next 
    next = previous + current #2

