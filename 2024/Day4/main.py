import re
total = 0
filename = "test_data.txt"
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

for listi in range(len(array)):
    for i in range(len(array[listi]) - 3):
        checkstring = get_point(i, listi) + get_point(i + 1, listi) + get_point(i + 2, listi) + get_point(i + 3, listi)
        if checkstring == "XMAS" or checkstring == "SAMX":
            total += 1

for listi in range(len(array) - 3):
    for i in range(len(array[listi])):
        checkstring = get_point(i, listi) + get_point(i, listi + 1) + get_point(i, listi + 2) + get_point(i, listi + 3)
        if checkstring == "XMAS" or checkstring == "SAMX":
            total += 1

for listi in range(len(array) - 3):
    for i in range(len(array[listi]) - 3):
        checkstring = get_point(i, listi) + get_point(i + 1, listi + 1) + get_point(i + 2, listi + 2) + get_point(i + 3, listi + 3)
        if checkstring == "XMAS" or checkstring == "SAMX":
            total += 1

for listi in range(3, len(array)):
    for i in range(len(array[listi]) - 3):
        checkstring = get_point(i, listi) + get_point(i + 1, listi - 1) + get_point(i + 2, listi - 2) + get_point(i + 3, listi - 3)
        if checkstring == "XMAS" or checkstring == "SAMX":
            total += 1


print("Part 1", total)

total = 0
file = open(filename)
for string in file:
    chars = []
    for char in string.strip():
        chars.append(char)
    array.append(chars)

rows = len(array)
cols = len(array[0])

# Define the X-MAS pattern checks
def check_x_mas(x, y):
    """Check all 8 possibilities of X-MAS at position (x, y)."""
    patterns = [
        # Forward "MAS" on both diagonals
        [(0, 0), (1, 1), (2, 2)],  # Primary diagonal
        [(2, 0), (1, 1), (0, 2)],  # Anti-diagonal
        # Reverse "SAM" on both diagonals
        [(2, 2), (1, 1), (0, 0)],
        [(0, 2), (1, 1), (2, 0)],
    ]
    valid = 0
    for p1, p2 in zip(patterns[:2], patterns[2:]):
        # Check MAS forward and backward on primary diagonal
        if all(get_point(x + dx, y + dy) == c for (dx, dy), c in zip(p1, "MAS")) and \
           all(get_point(x + dx, y + dy) == c for (dx, dy), c in zip(p2, "MAS")):
            valid += 1
            print("MAS")
    return valid

# Traverse the grid to count X-MAS patterns
for y in range(rows - 2):
    for x in range(cols - 2):
        total += check_x_mas(x, y)
        print(check_x_mas(x, y))

print("Part 2", total)