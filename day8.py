
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
    mappings = {}
    lines = open('day8.txt', 'r').readlines()
    inputs = lines[0:1]
    for line in inputs:
        values = line.split(' | ')[0].split(' ')
        #find the 1
        one = ''
        searching = True
        while searching:
            for val in values:
                if len(val) == 2:
                    mappings[val] = 1
                if len(val) == 3:
                    mappings[val] = 7
                if len(val) == 4:
                    mappings[val] = 4
                if len(val) == 7:
                    mappings[val] = 8
                if len(val) == 5:
                    print("found length 5")
                    sevenFour = []
                    for key in mappings:
                        if mappings[key] == 7 or mappings[key] == 4:
                            for letter in key:
                                sevenFour.append(letter)
                    sevenFour = set(sevenFour)
                    print(sevenFour)
                    print(val)
                    count = 0
                    for letter in sevenFour:
                        if letter in val:
                            count += 1
                    if count == 4:
                        mappings[val] = 5
            if len(mappings) == 5:
                searching = False

    print(mappings)

def getPossibleMappings(current, possible):
    new = []
    for val in current:
        if val in possible:
            new.append(val)
    return new
             
part2()