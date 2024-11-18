f0 = open('test.txt').read().split('\n')
f1 = open('notes3-1.txt').read().split('\n')
f2 = open('notes3-2.txt').read().split('\n')
f3 = open('notes3-3.txt').read().split('\n')

dr = [[0,1],[0,-1],[1,0],[-1,0]]   

# converts grid to numbers
def enumerateGrid(f):
    grd = []
    for r in f:
        line = []
        for c in r:
            if c == '#':
                line.append(1)
            else:
                line.append(0)
        grd.append(line)
    return grd

# returns true if the block can be dug
def canDig(r, c):
    if grid[r][c] == 0:
            return False
    
    dig = True
    for d in dr:
        if grid[r][c] > grid[r+d[0]][c+d[1]]:
            dig = False
    return dig

# iterates over entire grid and digs where it can
# returns true if no digging was done
def digLayer():
    done = True
    for r in range(1, len(grid)-1):
        for c in range(1, len(grid[r])-1):
            if canDig(r, c):
                grid[r][c] += 1
                done = False
    return done

# sums all numbers in grid
def count():
    t = 0
    for row in grid:
        t += sum(row)
    return t


grid = enumerateGrid(f1)
dn = False
while not dn:
    dn = digLayer()
print(count())


grid = enumerateGrid(f2)
dn = False
while not dn:
    dn = digLayer()
print(count())


grid = enumerateGrid(f3)
dr = [[0,1],[0,-1],[1,0],[-1,0],[-1,-1],[-1,1],[1,-1],[1,1]]   
dn = False
while not dn:
    dn = digLayer()
print(count())
