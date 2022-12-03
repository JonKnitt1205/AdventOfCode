def partOne():
    with open('2022/3/input.txt', 'r') as f:
        total = 0
        while True:
            line = f.readline()
            if line:
                first = line[:len(line)//2]
                second = line[len(line)//2:-1]
                match = ''
                for i in range(len(first)):
                    if first[i] in second:
                        match = first[i]
                        break
                if ord(match) <= 90:
                    total += 26
                    match = match.lower()
                total += (ord(match) - 96)     
            else:
                break
        return total

def partTwo():
    with open('2022/3/input.txt', 'r') as f:
        total = 0
        while True:
            group = []
            for i in range(3):
                line = f.readline()
                group.append(line)
            group.sort(key=len, reverse=True)
            if line:
                match = ''
                for i in range(len(group[0])):
                    if group[0][i] in group[1] and group[0][i] in group[2]:
                        match = group[0][i]
                        break
                if ord(match) <= 90:
                    total += 26
                    match = match.lower()
                total += (ord(match) - 96)     
            else:
                break
        return total

print(partOne())
print(partTwo())