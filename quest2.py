f = (open('notes2-1.txt').read().split('\n\n'))
runic = f[0].replace('WORDS:', '').split(',')
text = f[1]
t = 0

for i in range(0, len(runic)):
    t += text.count(runic[i])

# print(t)



# Part 2
# returns sum of runic symbols
def occurences(string, substrings):
    found = []
    for substring in substrings:
        pos = 0
        while pos <= len(string) - len(substring):
            if string[pos:pos+len(substring)] == substring:
                found.extend(range(pos, pos+len(substring)))
            pos += 1

    return len(set(found))

def addReversedStrings(list):
    for word in list:
        if word[::-1] not in list:
            list.append(word[::-1])
    return list

f = (open('notes2-2.txt').read().split('\n'))
text = f[2:]
runic = f[0].replace('WORDS:', '').split(',')
runic = addReversedStrings(runic)

t = 0
for phrase in text:
    t += occurences(phrase, runic)
# print(t)



# Part 3
f = open('notes2-3.txt').read().split('\n')
f = open('test.txt').read().split('\n')
text = f[2:]
runic = f[0].replace('WORDS:', '').split(',')
runic = addReversedStrings(runic)

def vertical(c):
    s = ''
    for ln in text:
        s += ln[c]
    return s

def removeDuplicates(OG):
    k = []
    for c in OG:
        if c not in k:
            k.append(c)
    return k

def occurences_2D(string, substrings):
    found = []
    for substring in substrings:
        pos = 0
        while pos <= len(string) - len(substring):
            if string[pos:pos+len(substring)] == substring:
                found.extend(range(pos, pos+len(substring)))
            pos += 1

    return found

coords = []
for i in range(len(text)):
    print(i, occurences_2D(text[i], runic))












with open("everybody_codes_e2024_q2_p3.txt") as f:
    top,_,*lines = f.read().splitlines()
words = top.split(":")[1].split(",")
words.extend([w[::-1] for w in words])
grid = [[False]*len(line) for line in lines]
for i,line in enumerate(lines):
    for j in range(len(line)):
        for word in words:
            l = len(word)
            if (line*2)[j:j+l] == word:
                for n in range(l):
                    grid[i][(j+n)%len(line)] = True
senil = list(map("".join,zip(*lines)))
for j,enil in enumerate(senil):
    for i in range(len(enil)):
        for word in words:
            l = len(word)
            if enil[i:i+l] == word:
                for n in range(l):
                    grid[i+n][j] = True
print(sum(map(sum,grid)))
