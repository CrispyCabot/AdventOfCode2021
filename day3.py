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

part1()