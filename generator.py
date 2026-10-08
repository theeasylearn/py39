import random as rd 
import string as st
def generateOTP(length=6):
    temp = ''
    for i in range(0,length):
        num = rd.randint(0,9)
        # print(num,end=' ')
        temp= temp + str(num)
    return temp 
def generatePassword(length=8):
    seeds = st.ascii_lowercase + st.ascii_uppercase + st.digits + "!@#$%^&*(){}+-*/"
    list = []
    for letter in seeds:
        list.append(letter)
    rd.shuffle(list)
    rd.shuffle(list)
    # print(list)
    return ''.join(list[0:length])
