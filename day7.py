
def day7():
    lines = open('day7.txt', 'r').readlines()
    inp = [int(i) for i in lines[0].split(',')]
    inp.sort()
    maxVal = inp[-1]
    minVal = inp[0]
    start = int(sum(inp) / len(inp))
    change = 1
    bestFuelUse = -1
    bestVal = 0
    useIncreaseCount = 0
    
    while minVal <= start <= maxVal:
        #get fuel use for start
        use = 0
        for i in inp:
            val = abs(i - start)
            use += sum([i for i in range(val+1)])
        if bestFuelUse == -1 or use < bestFuelUse:
            bestFuelUse = use
            bestVal = start
        if use > bestFuelUse:
            useIncreaseCount += 1
        # if useIncreaseCount >= 2:
        #     break

        start += change
        newChange = abs(change) + 1
        change = newChange if change < 0 else -newChange
    print(bestFuelUse, bestVal)

day7()