f1 = [(i[0], int(i[1:])) for i in open('notes14-1.txt').read().split(',')]
f2 = [[(i[0], int(i[1:])) for i in line.split(',')] for line in open('notes14-2.txt').read().split('\n')]
f3 = [[(i[0], int(i[1:])) for i in line.split(',')] for line in open('notes14-3.txt').read().split('\n')]

def grow(instructions):
    x,y,z = 0,0,0
    cds = set()
    for d, n in instructions:
        for _ in range(n):
            match d:
                case "U": y += 1
                case "D": y -= 1
                case "R": x += 1
                case "L": x -= 1
                case "F": z += 1
                case "B": z -= 1
            cds.add((x, y, z))
    return cds, (x,y,z)

print(max(y for x,y,z in grow(f1)[0]))
print(len(set().union(* (grow(insts)[0] for insts in f2))))

def findDist(start, targets, coords):
    seen = set([start])
    targets = set(targets)
    t = 0
    dist = 0
    border = set([start])

    while targets:
        newborder = set()
        for (x,y,z) in border:
            seen.add((x,y,z))
            if (x,y,z) in targets:
                t += dist
                targets.remove((x,y,z))
            for (dx,dy,dz) in [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]:
                nx,ny,nz = x+dx, y+dy, z+dz
                if (nx,ny,nz) in coords and (nx,ny,nz) not in seen:
                    newborder.add((nx,ny,nz))
        dist += 1
        border = newborder
    return t


blocks, leaves = set(), set()
for insts in f3:
    nblocks, nleaf = grow(insts)
    blocks |= nblocks
    leaves.add(nleaf)
trunk = [(x,y,z) for (x,y,z) in blocks if x == z == 0]
print(min(findDist(start, leaves, blocks) for start in trunk))

