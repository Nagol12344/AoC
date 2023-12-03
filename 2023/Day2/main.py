import re

games = []

red = r"[0-9]?[0-9]?[0-9]?[0-9] red"

file = open("real_data.txt")

for lines in file:
    count = 0
    lines = lines.strip().lower()
    reds = re.findall(r"[0-9]?[0-9]?[0-9]?[0-9] red", lines)
    greens = re.findall(r"[0-9]?[0-9]?[0-9]?[0-9] green", lines)
    blues= re.findall(r"[0-9]?[0-9]?[0-9]?[0-9] blue", lines)
    red, green, blue = [],[],[]
    colors = [reds,greens,blues]
    for color in colors:
        for number in color:
            if " red" in number: red.append(int(number.replace(" red", "")))
            if " green" in number: green.append(int(number.replace(" green", "")))
            if " blue" in number: blue.append(int(number.replace(" blue", "")))
    game = re.findall(r"game [0-9]?[0-9]?[0-9]?[0-9]", lines)
    check = 0
    if not max(red) > 12: check +=1
    if not max(green) > 13: check +=1
    if not max(blue) > 14: check +=1
    if check == 3: games.append(int(game[0].replace("game ", "")))

finalanswer = 0
for game in games:
    finalanswer += game

print("Part 1: "+str(finalanswer))

file = open("real_data.txt")

score = 0

for lines in file:
    lines = lines.strip().lower()
    reds = re.findall(r"[0-9]?[0-9]?[0-9]?[0-9] red", lines)
    greens = re.findall(r"[0-9]?[0-9]?[0-9]?[0-9] green", lines)
    blues= re.findall(r"[0-9]?[0-9]?[0-9]?[0-9] blue", lines)
    red, green, blue = [],[],[]
    colors = [reds,greens,blues]
    for color in colors:
        for number in color:
            if " red" in number: red.append(int(number.replace(" red", "")))
            if " green" in number: green.append(int(number.replace(" green", "")))
            if " blue" in number: blue.append(int(number.replace(" blue", "")))
    score += max(red)*max(green)*max(blue)

print("Part 2: "+str(score))