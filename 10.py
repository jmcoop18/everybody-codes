from collections import deque

map = [[int(char) for char in line] for line in open('10.txt').read().strip().splitlines()]

def score(r,c):
    q = deque([(r, c)])
    seen = {(r, c): 1}
    peaks = 0
    trails = 0
    while len(q) > 0:
        cr, cc = q.popleft()
        if map[cr][cc] == 9:
            trails += seen[(cr,cc)]

        for nr, nc in [(cr+1, cc), (cr, cc+1), (cr-1, cc), (cr, cc-1)]:
            if nr < 0 or nc < 0 or nr > len(map)-1 or nc > len(map)-1: continue
            if map[nr][nc] != map[cr][cc] + 1: continue
            
            if (nr, nc) in seen: 
                seen[(nr,nc)] += seen[(cr,cc)]
                continue
            seen[(nr,nc)] = seen[(cr,cc)]

            if map[nr][nc] == 9:
                peaks += 1
            q.append((nr, nc))
    return peaks, trails


trailheads = [(r,c) for r in range(len(map)) for c in range(len(map)) if map[r][c] == 0]
res = [(score(r,c)[0], score(r,c)[1]) for r,c in trailheads]

p1, p2 = 0, 0
for p,t in res:
    p1 += p
    p2 += t
print(p1)
print(p2)