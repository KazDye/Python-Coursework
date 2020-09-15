han = open('mbox-short.txt')
d = dict()
for lin in han:
    lin = lin.rstrip()
    wds = lin.split()
    if len(wds) < 1 :
        continue
    if wds[0] != 'From' :
        continue
    if wds[0] == 'From' :
        time = wds[5]
        hour = time.split(':')
        h = hour[0]
        d[h] = d.get(h,0) + 1
new = sorted(d.items())
for k, v in new :
    print (k, v)
