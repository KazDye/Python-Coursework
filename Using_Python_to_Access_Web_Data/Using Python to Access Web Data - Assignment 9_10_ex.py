han = open('intro.txt')

di = dict()
for lin in han:
    lin = lin.rstrip()
    wds = lin.split()
    for w in wds :
        di[w] = di.get(w,0) + 1

tmp = list()
for k,v in di.items() :
    newt = (v,k)
    tmp.append(nwt)


tmp = sorted(tmp, reverse=True)

for v,k in tmp[:5] :
    print(k,v)
