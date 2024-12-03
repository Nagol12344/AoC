file = open("test_data.txt").read()

print(file)

time = file[0]
distance = file[1]
times = []
distances = []
string = ""

for number in time: 
    if number in "0123456789":
        string+=number
    elif not string == "":
        times.append(string)
        string = ""

for number in distance: 
    if number in "0123456789":
        string+=number
    elif not string == "":
        distances.append(string)
        string = ""

print(times)
print(distances)