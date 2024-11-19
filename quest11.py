f0 = open('test.txt').read().split('\n')
f1 = open('notes11-1.txt').read().split('\n')
f2 = open('notes11-2.txt').read().split('\n')

def createDic(list):                               
    d = {}
    for i in list:
        id = i.split(':')
        d[id[0]] = id[1].split(',')
    return(d)

def newGen(curGen, days):
    for i in range(days):    
        new = []
        for l in curGen:
            new += [i for i in dic[l]]
        curGen = new
    return len(curGen)

dic = createDic(f1)
print(newGen('A', 4))

dic = createDic(f2)
print(newGen('Z', 10))



# ------------- Part 3 ------------- # 
from collections import defaultdict
f3 = open('notes11-3.txt').read().strip().split('\n')

rules = createDic(f3)
byType = {}
for ky in rules.keys():
    have = {ky: 1}
    for _ in range(20):
        newHave = defaultdict(int)
        for k,v in have.items():
            for x in rules[k]:
                newHave[x] += v
        have = newHave
    byType[ky] = sum(have.values())
print(max(byType.values()) - min(byType.values()))
