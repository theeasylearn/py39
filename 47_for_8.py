# for loop with numbers in reverse
# write a program to print multiplication table of given number in below format
# 5 x 10 = 50
# 5 x 9 = 45
# ..........
# 5 x 1 = 5
number = int(input("Enter number"))
for multiplier in range(10,0,-1):
    result = number * multiplier
    print(f"{number} X {multiplier} = {result}")

