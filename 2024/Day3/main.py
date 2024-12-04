import re
total = 0
filename = "real_data.txt"

file = open(filename)

for lines in file:
    muls = re.findall(r"mul\([0-9]*,[0-9]*\)", lines)
    for mul in muls:
        numbers = mul[4:-1]
        num = numbers.split(",")
        total+=int(num[0])*int(num[1])

print("Part 1:", total)


file = open(filename)
total = 0
dont = False
for lines in file:
    line = ""
    for i in range(len(lines)):
        if not dont:
            if lines[i] == "d":
                if lines[i+1] == "o":
                    if lines[i+2] == "n":
                        if lines[i+3] == "'":
                            if lines[i+4] == "t":
                                if lines[i+5] == "(":
                                    if lines[i+6] == ")":
                                        dont = True
                                    else: line=line+lines[i]
                                else: line=line+lines[i]
                            else: line=line+lines[i]
                        else: line=line+lines[i]
                    else: line=line+lines[i]
                else:
                    line=line+lines[i]
            else:
                line=line+lines[i]
        if dont:
            if lines[i] == "d":
                if lines[i+1] == "o":
                    if lines[i+2] == "(":
                        if lines[i+3] == ")":
                            dont = False
                            line=line+lines[i]
    muls = re.findall(r"mul\([0-9]*,[0-9]*\)", line)
    for mul in muls:
        numbers = mul[4:-1]
        num = numbers.split(",")
        total+=int(num[0])*int(num[1])

print(total)