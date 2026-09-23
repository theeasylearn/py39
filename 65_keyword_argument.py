def getMerit(maths,science,english,computer,drawing,history):
    print(f"maths = {maths} science = {science} english = {english} computer = {computer} drawing = {drawing} history = {history}")
    total = maths  + science + english;
    return total 
m = 100
s = 99
e = 98
c = 80
d = 70
h = 75
# wrong way of calling function
print(getMerit(c,d,h,m,s,e))

# perfect way of calling function
print(getMerit(history=h,drawing=d,computer=c,maths=m,science=s,english=e))
