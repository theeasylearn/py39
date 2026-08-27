#example of for loop 
# write a program to count odd and even numbers in list 
list = [11,25,10,40,49,101,150,200,199,300,305]
odd_count = 0 
even_count = 0
for num in list:
    if num%2==0: #even
        even_count = even_count + 1
    else:
        odd_count = odd_count + 1

print("Odd count = ",odd_count)
print("Even count = ",even_count)
