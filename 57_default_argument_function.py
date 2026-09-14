def getInches(meter,foot=0,inches=0):
    print(f"meter = {meter} foot = {foot} inches = {inches}")
    #convert meters into inches, foot into inches
    totalInch = (meter * 39.37) + (foot * 12) + inches
    return totalInch

totalInches = getInches(9,8,7)
print(f"total Inches of 3 argument = {totalInches}")
totalInches = getInches(9,8)
print(f"total Inches of 2 argument = {totalInches}")
totalInches = getInches(9)
print(f"total Inches of 1 argument = {totalInches}")
