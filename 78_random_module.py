import random as rd 
print("any float random number between 0 to 1 ",rd.random())
print("any float random number between 10 to 99 ",rd.uniform(10,99))
print("any integer random number between 10 to 99 ",rd.randint(10,99))
print("any integer random number between 10 to 100 divisible by 10 ",rd.randrange(10,100,10))

fruits = ['mango','banana','pineapple','orange','apple']
print("Pick any one random fruit ",rd.choice(fruits))
print("Pick any two random fruit ",rd.choices(fruits,k=2))

countries = ['India','China','Brzil','Australia','Canada','Japan','Russia']
rd.shuffle(countries)
print("Shuffled list ",countries)

colors = ['black','white','red','green','blue']
list = rd.sample(colors,5)
print(colors,list)