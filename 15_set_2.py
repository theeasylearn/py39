set1 = {1,2,3,4,5}
set2 = {3,4,5,6,7}

union = set1.union(set2) # combine two set but avoid duplicate values 
print("union = ",union)

intersection = set1.intersection(set2) # combine sets using only common values
print("intersection = ",intersection)

difference = set1.difference(set2) # all values which are in set1 but not in set 2
print(difference)

