point = 0
file = open("real_data.txt")

while line := file.readline():
    line = line.lstrip()
    if "X" in line: 
        player1=0
    elif "Y" in line: 
        player1=1
    elif "Z" in line:
        player1=2
    if "A" in line: 
        player2=0
    elif "B" in line: 
        player2=1
    elif "C" in line:
        player2=2

    winner = (3 + player1 - player2) % 3
    
    if winner == 1:point+=6
    if winner == 0:point+=3


    point += player1+1

print("Part 1: "+str(point))



point = 0
file = open("real_data.txt")

while line := file.readline():
    line = line.lstrip()
    if "X" in line:
        winner=2    
    elif "Y" in line: 
        winner=0
    elif "Z" in line:
        winner=1
    if "A" in line: 
        player2=0
    elif "B" in line: 
        player2=1
    elif "C" in line:
        player2=2
    else: print(line)

    if winner==0: player1=player2
    if winner==1:
        if player2==0: player1=1
        if player2==1: player1=2
        if player2==2: player1=0
    if winner==2:
        if player2==2: player1=1
        if player2==1: player1=0
        if player2==0: player1=2
    if winner == 1: point += 6 
    if winner == 2: point += 0
    if winner == 0: point += 3

    point += player1+1

print("Part 2:"+str(point))




