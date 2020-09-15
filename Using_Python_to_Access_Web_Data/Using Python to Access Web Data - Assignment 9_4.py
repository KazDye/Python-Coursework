han = open('mbox-short.txt')
most = dict()
for line in han:
    line = line.rstrip()
    wds = line.split()
    if len(wds) < 1 :
        continue
    if wds[0] != 'From' :
        continue
    if wds[0] == 'From' :
        words = wds[1]
        most[words] = most.get(words,0) + 1
bigcount = None
bigword = None
for x, count in most.items():
        if bigcount is None or count > bigcount:
            bigword = x
            bigcount = count
print(bigword,bigcount)
