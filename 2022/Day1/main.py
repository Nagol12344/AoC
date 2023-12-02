index = 1
count = 0
elfs = {}

file = open("real_data.txt")

while line := file.readline():
    line = line.lstrip()
    if not line == "": count += int(line)
    else: 
        elfs[str(index)] = count
        index+=1  
        count=0

count = 0
count += elfs.get(max(elfs, key=elfs.get))
del elfs[max(elfs, key=elfs.get)]

print("Part 1: "+str(count))

index = 1
count = 0
elfs = {}

file = open("real_data.txt")

while line := file.readline():
    line = line.lstrip()
    if not line == "": count += int(line)
    else: 
        elfs[str(index)] = count
        index+=1  
        count=0

count = 0
for i in range(3):
    count += elfs.get(max(elfs, key=elfs.get))
    del elfs[max(elfs, key=elfs.get)]

print("Part 2: "+str(count))