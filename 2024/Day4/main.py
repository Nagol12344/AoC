import re
total = 0
filename = "real_data.txt"
array = []
file = open(filename)

def get_point(x,y):
    try:
        return array[y][x]
    except:
        return "."

for string in file:
    chars = []
    for char in string.strip():
        chars.append(char)
    array.append(chars)



print(array)

for listi in range(len(array)):
    for i in range(len(array[listi])):
        checkstring = get_point(i,listi)+get_point(i+1,listi)+get_point(i+2,listi)+get_point(i+3,listi)
        if checkstring == "XMAS" or checkstring == "SAMX":
            total+=1
for listi in range(len(array)): #y
    for i in range(len(array[listi])): #x
        checkstring = get_point(i,listi)+get_point(i,listi+1)+get_point(i,listi+2)+get_point(i,listi+3)
        if checkstring == "XMAS" or checkstring == "SAMX":
            total+=1
for listi in range(len(array)): #y
    for i in range(len(array[listi])): #x
        checkstring = get_point(i,listi)+get_point(i+1,listi+1)+get_point(i+2,listi+2)+get_point(i+3,listi+3)
        if checkstring == "XMAS" or checkstring == "SAMX":
            total+=1
for listi in range(len(array)): #y
    for i in range(len(array[listi])): #x
        checkstring = get_point(i,listi)+get_point(i+1,listi-1)+get_point(i+2,listi-2)+get_point(i+3,listi-3)
        if checkstring == "XMAS" or checkstring == "SAMX":
            total+=1

print(total)