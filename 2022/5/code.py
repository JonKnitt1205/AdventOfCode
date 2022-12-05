def partOne():
    answer = ''
    with open("2022/5/input.txt", "r") as f:
        picture = []
        positions = []
        storage = []
        while True:
            line = f.readline()
            if line and line[0] != 'm':
                picture.append(line)
            else:
                break
        cols = 1
        while True:
            if str(cols) in picture[-2]:
                positions.append(picture[-2].index(str(cols)))
            else:
                cols -= 1
                break
            cols += 1
        for col in positions:
            storage.append([])
            for row in picture[:-2]:
                if(len(row) > col and row[col] != ' '):
                    storage[-1].insert(0, row[col])
        while True:
            repeats = int(line[line.index('move ') + 5:line.index(' from')])
            start = int(line[line.index('from ') + 5:line.index(' to')]) - 1
            end = int(line[line.index('to ') + 3:]) - 1
            for _ in range(repeats):
                storage[end].append(storage[start].pop(-1))
            line = f.readline()
            if not line:
                break
        for col in storage:
            answer += col[-1]
    return answer


def partTwo():
    answer = ''
    with open("2022/5/input.txt", "r") as f:
        picture = []
        positions = []
        storage = []
        while True:
            line = f.readline()
            if line and line[0] != 'm':
                picture.append(line)
            else:
                break
        cols = 1
        while True:
            if str(cols) in picture[-2]:
                positions.append(picture[-2].index(str(cols)))
            else:
                cols -= 1
                break
            cols += 1
        for col in positions:
            storage.append([])
            for row in picture[:-2]:
                if(len(row) > col and row[col] != ' '):
                    storage[-1].insert(0, row[col])
        while True:
            repeats = int(line[line.index('move ') + 5:line.index(' from')])
            start = int(line[line.index('from ') + 5:line.index(' to')]) - 1
            end = int(line[line.index('to ') + 3:]) - 1
            for i in range(repeats):
                storage[end].append(storage[start].pop(len(storage[start]) - repeats + i))
            line = f.readline()
            if not line:
                break
        for col in storage:
            answer += col[-1]
    return answer

print(partOne())
print(partTwo())