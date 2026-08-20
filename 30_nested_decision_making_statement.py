#write a program to convert 24 hours format time in 12 hours format time 
'''
    input : 15 hours output 3 PM 
    input : 09 hours output 3 AM 
    input : 18 hours output 6 PM 
'''
hours = input("Enter time in 24 hours format ")
#convert into integer 
hours = int(hours)
if hours<0 or hours>24:
    print("not a valid time")
else:
    if hours<12:
        print(hours," AM")

    if hours>=12:
        hours = hours - 12 
        print(hours," PM")

print("good bye")
