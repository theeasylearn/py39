# for loop with dictionary 
# findout total run of all players & display each player name and score 
player = {"Rohit Sharma": 9, "Virat Kohli": 76, "Rishabh Pant": 0, "Suryakumar Yadav": 3, "Axar Patel": 47, "Shivam Dube": 27, "Hardik Pandya": 5, "Ravindra Jadeja": 2}
total = 0
for key in player:
    print(key, "has made runs ",player[key])
    total = total + player[key]

print("total ",total)

#findout maximum score and player name who made it 
#findout minimum score and player name who made it 