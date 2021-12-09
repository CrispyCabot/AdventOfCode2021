
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
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    possibleMappings = {}
    for letter in letters:
        possibleMappings[letter] = ['top', 'topRight', 'topLeft', 'middle', 
        'bottom', 'bottomRight', 'bottomLeft']
    lines = open('day8.txt', 'r').readlines()
    inputs = lines[0:1]
    for line in inputs:
        inp = line.split('|')[0]
        for val in inp.split(' '):
            if len(val) == 2:
                for letter in val:
                    possibleMappings[letter] = getPossibleMappings(possibleMappings[letter], ['topRight', 'bottomRight'])
            elif len(val) == 3:
                for letter in val:
                    possibleMappings[letter] = getPossibleMappings(possibleMappings[letter], ['top', 'topRight', 'bottomRight'])
            elif len(val) == 4:
                for letter in val:
                    possibleMappings[letter] = getPossibleMappings(possibleMappings[letter], ['middle', 'topRight', 'bottomRight', 'topLeft'])
            elif len(val) == 7:
                for letter in val:
                    possibleMappings[letter] = getPossibleMappings(possibleMappings[letter], ['top', 'topRight', 'topLeft', 'middle', 'bottom', 'bottomRight', 'bottomLeft'])
    print(possibleMappings)

def getPossibleMappings(current, possible):
    new = []
    for val in current:
        if val in possible:
            new.append(val)
    return new
             
part2()