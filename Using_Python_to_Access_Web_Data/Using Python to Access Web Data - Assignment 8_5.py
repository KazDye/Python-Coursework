han = open('mbox-short.txt')
c = 0
for line in han:
    line = line.rstrip()
    wds = line.split()
    if len(wds) < 1 :
        continue
    if wds[0] != 'From' :
        continue
    if wds[0] == 'From' :
        c = c + 1
    print(wds[1])
print('There were', c, 'lines in the file with From as the first word')


#Example of Guardian you could use
#han = open('mbox-short.txt')
#for line in han:
#    line = line.rstrip()
#    print('Line:',line)
#    if line == '' :
#        # print('Skip Blank')
#        continue
#    wds = line.split()
#    print('Words:', wds)
#    if wds[0] != 'From' :
#        # print('Ignore')
#        continue
#    if wds[0] == 'From' :
#    print(wds[1])

#Example with Guardian Len statement
#han = open('mbox-short.txt')
#for line in han:
#   line = line.rstrip()
#   wds = line.split()
#   if len(wds) < 3 :
#       continue
#   if wds[0] != 'From' :
#       continue
#   print(wds[2])

#Example with Guardian Len statement combined
#Order matters here because the guardian must come before
#han = open('mbox-short.txt')
#for line in han:
#    line = line.rstrip()
#    wds = line.split()
#    if len(wds) < 3 or wds[0] != 'From' :
#        continue
#    print(wds[2])
