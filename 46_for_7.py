# for loop with numbers
# write a program to print multiplication table of given number in below format
# 5 x 1 = 5
# 5 x 2 = 10
# 5 x 3 = 15
number = 5
for multiplier in range(1,11):
    result = number * multiplier
    print(f"{number} X {multiplier} = {result}")

