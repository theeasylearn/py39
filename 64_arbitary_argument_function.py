# write a program to convert all the string values 
    # into lower case 
    # remove extra space 
    # replace space in between with _ (underscore)
    # replace - (dash) with _ (underscore)
# example 
# input : Car
#           Washing Machine 
#           top-down  
# output : car 
#           washing_machine 
#           top_down  
def convert(*words):
    #create empty list 
    list = [] 
    for word in words:
        temp = word.lower() #word convert lowercase
        temp = temp.strip() #remove extra space from both side (left & right)
        temp = temp.replace(" ","_") #replace ' ' with _
        temp = temp.replace("-","_") #replace '-' with _
        list.append(temp)
        # print(temp,end=' ')
    return list 

list = convert("Car","Washing Machine","top-down","Start"," Book ","god")
print(list)

