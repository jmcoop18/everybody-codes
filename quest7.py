f = open('notes7-1.txt').read().split('\n')

plans = []
for line in f:
    plans.append(line[0])
    plans.append(line[2:].split(','))    

dir = {'+' : 1, '=' : 0, '-' : -1}
# dir['+'] = 1

def run(list):
    rows = int(len(list)/2)
    res = ['', [10] for _ in range(rows)]
    for i in range(rows):
        print(i)
        # for d in i:
        #     print(i)
            # res[i][d] += dir[]

run(plans)
