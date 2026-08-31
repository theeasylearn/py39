# for loop with string 
# findout how many words string has 
# input : apple banana output : 2 words
# input : om namah shivay output : 3 words 
line = input("Enter your name to count words")
count = 1
for letter in line:
    if letter==" ":
        count = count + 1

print(f"{count} words")