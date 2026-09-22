def getMax(*numbers):
    #in arbitrary function *argument is always tuple (read only list)
    # print("-"*100)
    # print(len(numbers))
    # print(numbers)
    max = numbers[0] # 10
    for num in numbers:
        if max<num: #10>10
            max = num 
    return max


#calling getMax function
# getMax() # 0 arguments 
print("Maximum value ",getMax(10,5,20,17,35,25,100,50,200))
max = getMax(200,400,600,800,500,450)
print("Maximum value ",max)

