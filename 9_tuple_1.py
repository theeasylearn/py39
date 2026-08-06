#example of tuple 
gods = ("Bramha","Shiv","Vishnu")
devtas = ('indra','Agnidev','Vayudev','varundev')
print(gods)
print(devtas)
print(gods + devtas)
print(gods * 3)
print(gods[0]) #Bramha
print(gods[0:2]) #Bramha Shiv
print(gods[1:]) #Shiv Vishnu
# gods[1] = 'shiv shankar' #error because tuple immutable (read only)
print(gods)