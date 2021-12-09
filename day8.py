
def part1():
    lines = open('day8.txt', 'r').readlines()
    count = 0
    for line in lines:
        output = line.split('|')[1]
        for val in output.split(' '):
            if len(val) in [2, 3, 4, 7]:
                count += 1
    print(count)

def part2():
    possibleMappings = {}
    lines = open('day8.txt', 'r').readlines()
    for line in lines:
        inp = line.split('|')[0]
        for val in inp.split(' '):
            if val in possibleMappings:
                pass
                
part2()