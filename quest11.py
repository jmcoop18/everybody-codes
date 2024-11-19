f0 = open('test.txt').read().split('\n')
f1 = open('notes11-1.txt').read().split('\n')
f2 = open('notes11-2.txt').read().split('\n')
f3 = open('notes11-3.txt').read().split('\n')


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


dic = createDic(f3)
res = []
starts = []
# for start in dic:
#     res.append(newGen([start], 20))
# print(newGen(['PGG'], 20))