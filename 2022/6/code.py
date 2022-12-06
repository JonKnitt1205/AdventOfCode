def partOne(windowSize):
    with open('2022/6/input.txt') as f:
        line = f.readline()
        windowStart = 0
        while True:
            isKey = True
            for char in line[windowStart:windowStart + windowSize]:
                if line[windowStart:windowStart + windowSize].count(char) > 1:
                    isKey = False
                    break
            if isKey:
                return windowStart + windowSize
            windowStart += 1

print(partOne(4))
print(partOne(14))