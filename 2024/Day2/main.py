total = 0
filename = "real_data.txt"

file = open(filename)

# Check if the list is sorted
def if_list_is_sorted(a):
    if (all(a[i] <= a[i + 1] for i in range(len(a) - 1)) or all(a[i] >= a[i + 1] for i in range(len(a) - 1))):
        return True
    else: 
        if a == [1,3,4,5]:
            print("not sorted")
        return False

# Check if the list is valid
def list_is_valid(a, b):
    safe = True
    if not if_list_is_sorted(a):
        safe = False
    for i in range(len(b)-1):
        if not safe:
            break
        tmpnum = abs(int(b[i]) - int(b[i+1]))
        if tmpnum in [1, 2, 3]:
            continue
        else:
            safe = False
    return safe
# Check every line
for line in file:
    numbers = [int(i) for i in line.split(" ")]
    if list_is_valid(numbers, numbers):
        total += 1
    else:
        pass

print(f"Part 1: {total}")
    
total = 0
file.close()
file = open(filename)
# Loop v2
for line in file:
    numbers = [int(i) for i in line.split(" ")]
    if list_is_valid(numbers, numbers):
        total += 1
    else:
        passed = False
        for i in range(len(numbers)):
            copy = numbers.copy()
            del copy[i-1]
            if list_is_valid(copy, copy):
                total += 1
                passed = True
                break
            else:
                pass

print(f"Part 2: {total}")