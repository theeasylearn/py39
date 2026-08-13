
a = 10
b = 20
c = 30
d = 40

print(f"a = {a} b = {b} c = {c} d = {d}")

#we must logical operator between relational expression 
result = a < b and c < d  # 10 < 20 and 30 < 40
print(f"{result} = {a} < {b} and {c} < {d}")

result = b < a and c < d  
print(f"{result} = {b} < {a} and {c} < {d}")

result = c > a and c > d  
print(f"{result} = {c} > {a} and {c} > {d}")

result = c > a or c > d  
print(f"{result} = {c} > {a} or {c} > {d}")

result = a < b or a > d  
print(f"{result} = {a} < {b} or {a} > {d}")

result = not (a < b)
print(result)

result = not (a > b)
print(result)



