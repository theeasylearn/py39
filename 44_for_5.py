# for loop with string 
# findout how many letters string has 
# input : apple output : 5 letters 
# input : banana output : 6 letters 
line = input("Enter your name to count letters")
count = 0
for letter in line:
    # print(letter)
    count = count + 1

print(f"{count} letters")