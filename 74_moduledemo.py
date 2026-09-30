#import module
import mymath
import currency as cr 

num = int(input("Enter number for square and qube"))
square = mymath.getSquare(num)
print("square ",square)

print("Qube = ",mymath.getQube(num))

print(mymath.getPi())

print("100 rs = dollar ",cr.toDollar(100))
print("100 rs = Euro ",cr.toEuro(100))
print("100 rs = Pound ",cr.toPound(100))