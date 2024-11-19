f1 = list(map(int, open('notes4-1.txt').read().split('\n')))
f2 = list(map(int, open('notes4-2.txt').read().split('\n')))

def hammer(list, ht):
    t = 0
    for n in list:
        t += abs(n- ht)
    return(t)

mn = (min(f1))
print(hammer(f1, mn))

mn = (min(f2))
print(hammer(f2, mn))



f3 = list(map(int, open('notes4-3.txt').read().split('\n')))
best = float('inf')
for h in range(min(f3), max(f3)):
    strikes = hammer(f3, h)
    if strikes < best:
        best = strikes
print(best)
