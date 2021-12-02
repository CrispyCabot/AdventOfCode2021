def part1():
    lines = open("day1_1.txt", "r").readlines();
    last = int(lines[0].strip())
    count = 0
    for line in lines:
        curr = int(line.strip())
        if curr > last:
            count += 1
        last = curr
    print(count)

def part2():
    lines = open("day1_2.txt", "r").readlines();
    for i, val in enumerate(lines):
        lines[i] = int(val.strip())
    last = sum(lines[0:3])
    count = 0
    for i in range(0, len(lines)-2):
        new = sum(lines[i:i+3])
        if new > last:
            count += 1
        last = new
    print(count)

part2()