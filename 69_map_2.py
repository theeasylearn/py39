numbers = [1,2,3,4,5,6,7,8,9,10]
evens = filter(lambda num: num%2==0,numbers)
print(list(evens))

numbers = [100,80,75,90,45,40,31,65]
#numbers which are above 50
fifty = filter(lambda item: item>50,numbers)
print(list(fifty))

#numbers which are in range of 30 to 60
range = filter(lambda item: item>=30 and item<=60,numbers)
print(list(range))
