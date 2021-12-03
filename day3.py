def part1():
    lines = open("day3_1.txt", "r").readlines();
    gamma = ''
    epsilon = ''
    for i, val in enumerate(lines):
        lines[i] = val.strip()
    for i in range(len(lines[0])):
        zeroCount = 0
        oneCount = 0
        for line in lines:
            if line[i] == '1':
                oneCount += 1
            elif line[i] == '0':
                zeroCount += 1
        if zeroCount > oneCount:
            gamma += '0'
            epsilon += '1'
        else:
            gamma += '1'
            epsilon += '0'
    
    print(int(gamma, 2) * int (epsilon, 2))

def part2():
    lines = open("day3_1.txt", "r").readlines();
    for i, val in enumerate(lines):
        lines[i] = val.strip()
    oxygen = lines.copy()
    co2 = lines.copy()
    for i in range(len(oxygen[0])):
        if len(oxygen) == 1:
            break
        zeroCount = 0
        oneCount = 0
        for line in oxygen:
            if line[i] == '1':
                oneCount += 1
            elif line[i] == '0':
                zeroCount += 1
        keep = '1'
        if zeroCount > oneCount:
            keep = '0'
        removals = []
        for line in oxygen:
            if line[i] != keep:
                removals.append(line)
        for line in removals:
            oxygen.remove(line)
    for i in range(len(co2[0])):
        if len(co2) == 1:
            break
        zeroCount = 0
        oneCount = 0
        for line in co2:
            if line[i] == '1':
                oneCount += 1
            elif line[i] == '0':
                zeroCount += 1
        keep = '1'
        if zeroCount <= oneCount:
            keep = '0'
        removals = []
        for line in co2:
            if line[i] != keep:
                removals.append(line)
        for line in removals:
            co2.remove(line)
    print(int(oxygen[0], 2) * int(co2[0], 2))

part2()