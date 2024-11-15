f = (open('notes2-1.txt').read().split('\n\n'))
runic = f[0].replace('WORDS:', '').split(',')
text = f[1]
t = 0

for i in range(0, len(runic)):
    t += text.count(runic[i])

# print(t)



# Part 2
f = (open('notes2-2.txt').read().split('\n'))
runic = f[0].replace('WORDS:', '').split(',')
text = f[2:]
t = 0

def occurences(string, substring):
    t = 0
    pos = 0
    while pos <= len(string) - len(substring):
        if string[pos:pos+len(substring)] == substring:
            t += 1
        pos += 1
    return t

for word in runic:
    if word[::-1] not in runic:
        runic.append(word[::-1])

for line in text:
    found = []
    for word in runic:
        runicLength = len(word)
        prev = 0

        for i in range(occurences(line, word)):
            idx = line.index(word, prev)
            found.extend(range(idx, idx + runicLength))
            prev = found[1-runicLength]    
    
    t += (len(set(found)))
    
print(t)

