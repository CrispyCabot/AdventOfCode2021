class Spot:
    def __init__(self, val):
        self.val = val
        self.marked = False
    def __str__(self):
        return self.val

def part1():
    lines = open("day4.txt", "r").readlines();

    inputs = lines.pop(0)

    boards = []
    currBoard = []
    for line in lines:
        if line == '\n':
            boards.append(currBoard)
            currBoard = []
            continue
        row = []
        for val in line.strip().split():
            row.append(Spot(int(val)))
        currBoard.append(row)
    boards.append(currBoard)
    
    #first appended thing will be the empty list
    boards.pop(0)

    inputs = list(map(int, inputs.split(',')))
    for inp in inputs:
        for board in boards:
            for row in board:
                for spot in row:
                    if spot.val == inp:
                        spot.marked = True

        #check if a board has bingo
        hasBingo = False
        for board in boards:
            #check rows
            for row in board:
                bingo = True
                for spot in row:
                    if not spot.marked:
                        bingo = False
                        break
                if bingo:
                    hasBingo = True
            #check columns
            for i in range(len(board[0])):
                bingo = True
                for row in board:
                    if not row[i].marked:
                        bingo = False
                        break
                if bingo:
                    hasBingo = True
            #check diagonals
            bingo = True
            for i in range(5):
                if not board[i][i].marked:
                    bingo = False
            if bingo:
                hasBingo = True
            for i in range(5):
                if not board[i][4-i].marked:
                    bingo = False
            if bingo:
                hasBingo = True

            if hasBingo:
                unmarkedSum = 0
                for row in board:
                    for spot in row:
                        if not spot.marked:
                            unmarkedSum += spot.val
                print(unmarkedSum * inp)
                break
        if hasBingo:
            break

def checkBingo(board):
    hasBingo = False
    #check rows
    for row in board:
        bingo = True
        for spot in row:
            if not spot.marked:
                bingo = False
                break
        if bingo:
            hasBingo = True
    #check columns
    for i in range(len(board[0])):
        bingo = True
        for row in board:
            if not row[i].marked:
                bingo = False
                break
        if bingo:
            hasBingo = True
    #check diagonals
    bingo = True
    for i in range(5):
        if not board[i][i].marked:
            bingo = False
    if bingo:
        hasBingo = True
    for i in range(5):
        if not board[i][4-i].marked:
            bingo = False
    return hasBingo

def part2():
    lines = open("day4.txt", "r").readlines();

    inputs = lines.pop(0)

    boards = []
    currBoard = []
    for line in lines:
        if line == '\n':
            boards.append(currBoard)
            currBoard = []
            continue
        row = []
        for val in line.strip().split():
            row.append(Spot(int(val)))
        currBoard.append(row)
    boards.append(currBoard)
    
    #first appended thing will be the empty list
    boards.pop(0)

    inputs = list(map(int, inputs.split(',')))
    lastWinningInp = 0
    lastWinningBoard = []
    for inp in inputs:
        for board in boards:
            for row in board:
                for spot in row:
                    if spot.val == inp:
                        spot.marked = True

        #check if a board has bingo then remove it
        removals = []
        hasBingo = False
        for index, board in enumerate(boards):
            if checkBingo(board):
                removals.append(board)
                lastWinningBoard = board
                lastWinningInp = inp
        for removal in removals:
            boards.remove(removal)
        print(len(boards))
    unmarkedSum = 0
    for row in lastWinningBoard:
        for spot in row:
            if not spot.marked:
                unmarkedSum += spot.val

    for row in lastWinningBoard:
        for spot in row:
            if spot.marked:
                print('*', end='')
            print(str(spot.val) + ' ', end='')
        print()
    print()
    print(unmarkedSum, lastWinningInp)
    print('val', unmarkedSum * lastWinningInp)

part2()