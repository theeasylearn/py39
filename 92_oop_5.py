#example of class 
class Society:
    #class type variable 
    CommunityHall = "Ganesh Community Hall"
    NoOfGates = 2
    #define constructor 
    def __init__(self,flatno,owner):
        #create instance variable
        self.flatno = flatno
        self.owner = owner
    def display(self):
        print("Flat No ",self.flatno)
        print("Owner ",self.owner)
        print("Community Hall Name ",Society.CommunityHall)
        print("No of gates ",Society.NoOfGates)
        
#create object
s1 = Society(104,"Ankit Patel") #it will call constructor automatically
s2 = Society(105,"Diya Patel") #it will call constructor automatically
s3 = Society(106,"Jiya Patel") #it will call constructor automatically

s1.display()
s2.display()
s3.display()
print(Society.CommunityHall)
print(Society.NoOfGates)

#change class variable using classname
Society.CommunityHall = "Shiv Community Hall"
Society.NoOfGates = 3
print(Society.CommunityHall)
print(Society.NoOfGates)

#accessing class variable using object
print(s1.CommunityHall)
print(s2.NoOfGates)