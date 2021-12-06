
def day6():
    lines = open('day6.txt', 'r').readlines()
    allFish = [int(i) for i in lines[0].split(',')]
    sizes = {}
    keys = [i for i in range(-1,9)]
    for key in keys:
        sizes[key] = 0
    #get count of each element
    for inp in allFish:
        sizes[inp] += 1
    for day in range(256):
        print(f'day {day}')
        for key in keys:
            if key == -1:
                continue
            sizes[key-1] = sizes[key]
        sizes[6] += sizes[-1]
        sizes[8] = sizes[-1]
    total = 0
    for key in range(9):
        if key != -1:
            total += sizes[key]
    print(total)
    #350917

day6()