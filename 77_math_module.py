#example math module
import math 
amount = 123.4567
amount_2 = -123.12

print(f"{amount} ceil value ",math.ceil(amount)) #124
print(f"{amount} floor value ",math.floor(amount)) #123
print(f"{amount} truncated value ",math.trunc(amount)) #123
print(f"{amount} round value ",round(amount,2)) #123.45
print(f"{amount_2} absolute value ",math.fabs(amount_2)) #123
print(f"factorial of 5 ",math.factorial(5)) #120
print(f"power 5 of rest 3 ",math.pow(5,3)) # 5 x 5 x 5 
print(f"copy sign function of 5 and - 3",math.copysign(5,-3)) # -5
print(f"copy sign function of -5 and 3",math.copysign(-5,3)) # 5
