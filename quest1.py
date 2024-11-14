def countPotions(notes, n):
    f = open(notes).read()
    f = [f[i:i+n] for i in range(0, len(f), n)]
    t = 0

    for group in f:
        t += group.count('B') + 3*group.count('C') + 5*group.count('D')
        enemies = n - group.count('x')
        t += enemies * (enemies-1)

    return(t)

print(countPotions('notes1-1.txt.', 1))
print(countPotions('notes1-2.txt.', 2))
print(countPotions('notes1-3.txt.', 3))