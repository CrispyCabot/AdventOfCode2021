
def part1():
    lines = open("day9.txt", "r").readlines()
    for index, line in enumerate(lines):
        lines[index] = line.strip()
    lowPoints = []
    for index, line in enumerate(lines):
        for index2, number in enumerate(line):
            val = int(number)
            #check left
            if index2 > 0 and int(lines[index][index2-1]) <= val:
                continue
            #check right
            if index2 < len(line)-1 and int(lines[index][index2+1]) <= val:
                continue
            #check above
            if index > 0 and int(lines[index-1][index2]) <= val:
                continue
            #check below
            if index < len(lines)-1 and int(lines[index+1][index2]) <= val:
                continue
            lowPoints.append(val)
    total = 0
    for val in lowPoints:
        total += val + 1
    print(total)

part1()