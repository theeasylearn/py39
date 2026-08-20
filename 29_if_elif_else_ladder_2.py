'''
write a program to findout person's obesity level using BMI(body to mass index) technique. and display obesity level of person as below rule 
obesity level 
    Extremely Obese: BMI 35.0 and above
    Obese: BMI between 30.0  34.9
    Overweight: BMI between 25.0  29.9
    Normal: BMI between 18.5 to 24.9
    Underweight: BMI less than 18.5
    ---------------------------------------------------------------------
    formula to calculate BMI IS 
    bmi = weight(Kg ) / (height_in_meter * height_in_meter)
    
    input:
        weight, foot, inch 
    steps 
    1   accept input weight, foot, inch
    2   convert foot and inches into total inch 
    3   total inch convert into meter 
    5   calculate BMI 
    5   calculate & display person obesity level
'''
weight = float(input("Enter your weight in KG."))
print("Enter your height in foot & remaining inches")
foot = int(input("Enter only foot"))
inches = int(input("Enter remaining inches"))

total_inches = (foot * 12) + inches 
meter = total_inches / 39.37
bmi = round(weight / (meter * meter),2)
print(bmi)

if bmi>=25 and bmi<=29.99:
    print("you are Overweight")
elif bmi>=18.5 and bmi<=24.99:
    print("you are normal")
elif bmi>=30 and bmi<=34.99:
    print("you are Obese")
elif bmi>=35:
    print("you are extremely Obese")
else:
    print("you are underweight")

print("Good bye.")



