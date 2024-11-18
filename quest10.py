def availableSymbol(r, c, g):
    row = set(g[r][:2] + g[r][-2:])
    column = set(g[0][c] + g[1][c] + g[6][c] + g[7][c])
    return list(row & column)[0]

def runicWord(g):
    word = ''
    for r in range(2, 6):
        for c in range(2, 6):
            word += availableSymbol(r, c, g)
    return word

def power(string):
    t = 0
    for i in range(1, len(string) + 1):
        t += i * (ord(string[i-1]) - 64)
    return t

# Part 1
grid1 = open('notes10-1.txt').read().split('\n')
for r in range(len(grid1)):
    grid1[r] = [char for char in grid1[r]]

print(runicWord(grid1))


# Part 2
og = open('notes10-2.txt').read().split('\n\n')
shrines = []
for k in range(7):
    temp = og[k].split() # each row of boards
    for j in range(15):
        board = []
        for i in range(8):
            board.append(temp[(i * 15) + j])
        shrines.append(board)

t = 0
for grid in shrines:
    t += power(runicWord(grid))
print(t)