list1 = []
list2 = []
total = 0
filename = "real_data.txt"
file = open(filename)

for lines in file:
    lines = lines.strip()
    list1.append(int(lines.split("   ")[0]))
    list2.append(int(lines.split("   ")[1]))


list1.sort()
list2.sort()

for i in range(len(list1)):
    total += abs(list1[i]-list2[i])

print("Part 1:"+str(total))



list1 = []
list2 = []
total = 0

file = open(filename)

for lines in file:
    lines = lines.strip()
    list1.append(int(lines.split("   ")[0]))
    list2.append(int(lines.split("   ")[1]))

for number in list1:
    total+=list2.count(number)*number

print("Part 2:"+str(total))