#write a program to convert given minutes into hours and remaining minutes
# input : minutes : 195 output : 3 hours and 15 minutes 
minutes = int(input("Enter minutes"))

#convert minutes into hours 
hours = minutes // 60
minutes = minutes % 60
print("hours =",hours," minutes =",minutes)
