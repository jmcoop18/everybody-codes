# Part 1
f = open('notes1-1.txt').read()
ans = f.count('B') + 3*f.count('C')
print(f'Part 1 - {ans}')


# Part 2
f = open('notes1-2.txt').read()
f = [f[i:i+2] for i in range(0, len(f), 2)]

t = 0
for pair in f:
    if 'x' in pair:
        t += pair.count('B') + 3*pair.count('C') + 5*pair.count('D')
    else:
        t += 2 
        t += pair.count('B') + 3*pair.count('C') + 5*pair.count('D')
print(t)



def countPotions(notes, n):
    f = open(notes).read()
    f = [f[i:i+n] for i in range(0, len(f), n)]
    t = 0

    for enemies in f:
        t += pair.count('B') + 3*pair.count('C') + 5*pair.count('D')

        if f.count('x') == 0:
            t += 6
        elif f.count('x') == 1:
            t += 2

    return(t)

# print(countPotions('notes1-1.txt.', 1))
test = 'A'
print(test.count('x'))


A   C   B   A   B
0   3   1   0   1

Ax  AC  AD  Dx  xB
0   3+2 5+2 5   3

BDx ACC xxD AAB CxA
6+2 6+6 5   3+6 3+2