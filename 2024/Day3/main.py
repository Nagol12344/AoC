import re
total = 0
filename = "test_data.txt"

file = open(filename)

for lines in file:
    muls = re.findall(r"mul\([0-9]*,[0-9]*\)", lines)
    for mul in muls:
        numbers = mul[4:-1]
        num = numbers.split(",")
        total+=int(num[0])*int(num[1])

print("Part 1:", total)


