def part1():
    lines = open("day2_1.txt", "r").readlines();
    horizontal = 0
    depth = 0
    for line in lines:
        direction, amt = line.split(' ')
        amt = int(amt)

        if direction == 'forward':
            horizontal += amt
        if direction == 'down':
            depth += amt
        if direction == 'up':
            depth -= amt

    print(horizontal * depth)

def part2():
    lines = open("day2_2.txt", "r").readlines();
    horizontal = 0
    depth = 0
    aim = 0
    for line in lines:
        direction, amt = line.split(' ')
        amt = int(amt)

        if direction == 'forward':
            horizontal += amt
            depth += aim * amt
        if direction == 'down':
            aim += amt
        if direction == 'up':
            aim -= amt

    print(horizontal * depth)

part2()