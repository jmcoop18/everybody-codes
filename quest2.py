f = (open('notes2-1.txt').read().split('\n\n'))
runic = f[0].replace('WORDS:', '').split(',')
text = f[1]
t = 0

for i in range(0, len(runic)):
    t += text.count(runic[i])

# print(t)



f = (open('test.txt').read().split('\n'))
runic = f[0].replace('WORDS:', '').split(',')
text = f[2:]
t = 0

for word in runic:
    if word[::-1] not in runic:
        runic.append(word[::-1])

for line in text:
    found = ''
    for i in range(0, len(runic)):
        if runic[i] in line:
            found += (runic[i])
        # print(runic[i][::-1])

    # print(found)
    break


    # t += len(set(found))
    
# print(t)



