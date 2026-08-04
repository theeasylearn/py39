# write a program to accept 5 subject marks from user. calculate total marks & average and display it 
# science, maths, social, computer, history
science = input("Enter science marks") #50
maths = input("Enter maths marks")
social = input("Enter social marks")
computer = input("Enter computer marks")
history = input("Enter history marks")

#convert marks into integer
science = int(science) #now science has integer value
maths = int(maths)
social = int(social)
computer = int(computer)
history = int(history)

#process 
total = science + maths + social + computer + history
average = total / 5 

print("total = ",total)
print(f"average = {average}")