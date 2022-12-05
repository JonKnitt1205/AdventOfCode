def partOne():
    total = 0
    with open("2022/4/input.txt", "r") as f:
        while True:
            line = f.readline()
            if line:
                range1 = []
                for i in range(
                    int(line[:line.index('-')]), 
                    int(line[line.index('-') + 1:line.index(',')]) + 1
                    ):
                    range1.append(i)
                range2 = []
                line = line[line.index(',') + 1:]
                for i in range(
                    int(line[:line.index('-')]), 
                    int(line[line.index('-') + 1:]) + 1
                    ):
                    range2.append(i)

                if (range1[0] in range2 and range1[-1] in range2) or (range2[0] in range1 and range2[-1] in range1):
                    total += 1
            else:
                break
    return total


def partTwo():
    total = 0
    with open("2022/4/input.txt", "r") as f:
        while True:
            line = f.readline()
            if line:
                range1 = []
                for i in range(
                    int(line[:line.index('-')]), 
                    int(line[line.index('-') + 1:line.index(',')]) + 1
                    ):
                    range1.append(i)
                range2 = []
                line = line[line.index(',') + 1:]
                for i in range(
                    int(line[:line.index('-')]), 
                    int(line[line.index('-') + 1:]) + 1
                    ):
                    range2.append(i)

                if (range1[0] in range2 or range1[-1] in range2) or (range2[0] in range1 or range2[-1] in range1):
                    total += 1
            else:
                break
    return total

print(partOne())
print(partTwo())