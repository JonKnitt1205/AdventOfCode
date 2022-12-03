def partOne():
    with open("2022/2/input.txt", "r") as f:
        score = 0
        while True:
            line = f.readline()
            if line:
                if(line[2] == 'X'): # chose rock
                    score+= 1
                    if(line[0] == 'C'): # won, they chose scissors
                        score+= 6
                    elif(line[0] == "A"): # draw, they chose rock
                        score+= 3
                elif(line[2] == 'Y'): # chose paper
                    score+= 2
                    if(line[0] == 'A'): # won, they chose rock
                        score+= 6
                    elif(line[0] == "B"): # draw, they chose paper
                        score+= 3
                elif(line[2] == 'Z'): # chose scissors
                    score+= 3
                    if(line[0] == 'B'): # won, they chose paper
                        score+= 6
                    elif(line[0] == "C"): # draw, they chose scissors
                        score+= 3
            else:
                break # eof reached
        return score

def partTwo():
    with open("2022/2/input.txt", "r") as f:
        score = 0
        while True:
            line = f.readline()
            if line:
                if(line[2] == 'X'): # need to lose
                    if(line[0] == 'A'): # they chose rock, choose scissors to lose
                        score+= 3
                    elif(line[0] == "B"): # they chose paper, choose rock to lose
                        score+= 1
                    elif(line[0] == "C"): # they chose scissors, choose paper to lose
                        score+= 2
                elif(line[2] == 'Y'): # need to draw
                    score+= 3
                    if(line[0] == 'A'): # they chose rock, choose rock to draw
                        score+= 1
                    elif(line[0] == "B"): # they chose paper, choose paper to draw
                        score+= 2
                    elif(line[0] == "C"): # they chose scissors, choose scissors to draw
                        score+= 3
                elif(line[2] == 'Z'): # need to win
                    score+= 6
                    if(line[0] == 'A'): # they chose rock, choose paper to win
                        score+= 2
                    elif(line[0] == "B"): # they chose paper, choose scissors to win
                        score+= 3
                    elif(line[0] == "C"): # they chose scissors, choose rock to win
                        score+= 1
            else:
                break # eof reached
        return score

print(partOne())
print(partTwo())