'''
write a program to findout which farm is bigger in size from 2 farm's dimensions (length & width)
'''
print("Enter 1st farm length and width")
length_1 = input("Enter length")
width_1 = input("Enter width")

print("Enter 2nd farm length and width")
length_2 = input("Enter length")
width_2 = input("Enter width")

#convert it into float 
length_1 = float(length_1)
width_1 = float(width_1)

length_2 = float(length_2)
width_2 = float(width_2)

#process (calculate area )
area_1 = length_1 * width_1 #area_1 has 1st farm area
area_2 = length_2 * width_2 #area_2 has 2nd farm area 
print(f"area of 1st farm = {area_1} \narea of 2nd farm = {area_2}")
if area_1>area_2:
    print("1st farm is bigger then 2nd farm")
else:
    print("2nd farm is bigger then 1st farm")

print("Good bye.")