import re
totallist = []
total = 0
filename = "real_data.txt"

rules = []
books = []

file = open(filename)

for line in file:
    if line.strip() == "": break
    rules.append(line.strip().split("|"))
for line in file:
    books.append(line.strip().split(","))

for book in books:
    correct = True
    for rule in rules:
        if correct == False: break
        if rule[0] in book and rule[1] in book:
            if book.index(rule[0]) > book.index(rule[1]):
                correct = False
    if correct == True:
        totallist.append(book)
        #books.remove(book)

for list in totallist:
    total+= int(list[int(len(list)/2)])
    books.remove(list)

print("Part 1:", total)
total = 0

for book in books:
    for rule in rules:
        if rule[0] in book and rule[1] in book:
            if book.index(rule[0]) > book.index(rule[1]):
                book.remove(rule[0])
                book.insert(book.index(rule[1]), rule[0])
for book in books:
    for rule in rules:
        if rule[0] in book and rule[1] in book:
            if book.index(rule[0]) > book.index(rule[1]):
                book.remove(rule[0])
                book.insert(book.index(rule[1]), rule[0])
for book in books:
    for rule in rules:
        if rule[0] in book and rule[1] in book:
            if book.index(rule[0]) > book.index(rule[1]):
                book.remove(rule[0])
                book.insert(book.index(rule[1]), rule[0])
for list in books:
    total+= int(list[int(len(list)/2)])

print("Part 2", total)