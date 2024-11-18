f1 = open('notes3-1.txt').read().split('\n')
f2 = open('notes3-2.txt').read().split('\n')

dr = [[0,1],[0,-1],[1,0],[-1,0]]

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

print(enumerateGrid(f1))