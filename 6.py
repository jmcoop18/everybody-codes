grid = list(map(list, open('test.txt').read().strip().splitlines()))

def loop(r,c):
    nr, nc = -1, 0
    seen = set()

    while True:
        seen.add((r,c))
        if r + nr < 0 or c + nc < 0 or r + nr >= len(grid) or c + nc >= len(grid): return False
        if grid[r + nr][c + nc] == '#':
            nr, nc = nc, -nr
        else:
            r += nr
            c += nc
        if (r, c, nr, nc) in seen:
            return True

for row in range(len(grid)):
    for col in range (len(grid)):
        if grid[row][col] == '^':
            sr, sc = row, col
            break
 
t = 0

for cr in range(len(grid)):
    for cc in range(len(grid)):
        if grid[cr][cc] != '.': continue
        grid[cr][cc] = '#'
        if loop(sr,sc): 
            t += 1
        grid[cr][cc] = '.'

print(t)