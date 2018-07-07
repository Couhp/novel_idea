from random import randint
import time
import math

data = [x.rstrip() for x in open("idea.dat",'r').readlines()]

choose = []
KEY =5
while len(choose) <= KEY :
    index = randint(0, len(data))
    if index not in choose :
        choose.append(index)

for i in range(len(choose)) :
    if i == 0 :
        print ("$$ ", data[choose[i]], " $$")
    else :
        print("   ", data[choose[i]])
