def getCal(currentElf):
    return currentElf[1]

myElves = [[0, 0]]
with open('dayOneInput.txt', "r") as f:
    while True:
        line = f.readline()
        if line:
            try:
                myElves[-1][1] += int(line) 
            except:
                myElves.append([myElves[-1][0] + 1, 0])
        else:
            break # eof reached
    myElves.sort(key=getCal, reverse=True)
    
    # part 1
    print(myElves[0][1])
    
    # part 2
    total = 0
    for i in range(3):
        total += myElves[i][1]
    print(total)