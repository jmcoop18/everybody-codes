f = open('notes14-1.txt').read().split(',')

mx = 0
ht = 0
for d in f:
    if d[0] == 'U':
        ht += int(d[1:])
    elif d[0] == 'D':
        ht -= int(d[1:])
    if ht > mx:
        mx = ht  
# print(mx)



f = [l.split(',') for l in open('notes14-2.txt').read().split('\n')]

cds = {(0,0,0)}
for ln in f:
    for d in ln:
        x, y, z = 0, 0, 0
        if d[0] == 'U':
            y += int(d[1:])
        elif d[0] == 'D':
            y -= int(d[1:])
        elif d[0] == 'R':
            x += int(d[1:])
        elif d[0] == 'L':
            x -= int(d[1:])
        elif d[0] == 'F':
            z += int(d[1:])
        elif d[0] == 'B':
            z -= int(d[1:])
        cds.add((x, y, z))
print(len(cds))