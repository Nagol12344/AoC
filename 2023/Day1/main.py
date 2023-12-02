prenumbers = []
numbers = []
total = 0

file = open("real_data.txt")

for lines in file:
    lines = lines.strip()
    letters = list(lines)
    for letter in letters:
        if letter in "0123456789":
            prenumbers.append(letter)
    numbers.append(prenumbers[0]+prenumbers[len(prenumbers)-1])
    prenumbers = []

for number in numbers: total += int(number) 

print("Part 1:"+str(total))

prenumbers = []
numbers = []
total = 0

file = open("real_data.txt")

for lines in file:
    lines = lines.strip()
    lines = lines.replace("one", "o1e").replace("two", "t2o").replace("three", "t3e").replace("four", "f4r").replace("five", "f5e").replace("six", "s6x").replace("seven", "s7n").replace("eight", "e8t").replace("nine", "n9e")
    letters = list(lines)
    for letter in letters:
        if letter in "0123456789":
            prenumbers.append(letter)
    numbers.append(prenumbers[0]+prenumbers[len(prenumbers)-1])
    prenumbers = []
    

for number in numbers: total += int(number) 
print("Part 2:"+str(total))

