#write a program to convert given amount into words 
# input : amount : 12 output : one two
# input : amount : 45 output : four five
# input : amount : 78 output : seven eight
amount = int(input("Enter 2 digit amount")) #78
first_digit = amount // 10
last_digit = amount % 10
#create list
list = ['zero','one','two','three','four','five','six','seven','eight','nine']
#         0      1     2     3 
# print("first digit ",first_digit)
# print("last digit ",last_digit)
print(list[first_digit] + " " + list[last_digit]) 
