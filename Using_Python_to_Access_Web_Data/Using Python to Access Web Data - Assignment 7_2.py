fname = input('Enter file name: ')
try:
    fn = open(fname)
except:
    input('Invalid file:', fname)
    quit()
c = 0
fz = 0
for x in fn :
    if x.startswith('X-DSPAM-Confidence:'):
        ft = 'X-DSPAM-Confidence:'
        #So we can count the string
        fu = len(ft)
        #Count characters in ft
        fv = int(fu)
        #must convert to int in order for use in fy
        fw = x.startswith('X-DSPAM-Confidence:')
        fx = x.find('/n', fw)
        #/n will always come at the end of the line
        #This function will find /n after fw
        fy = x[fw+fv : fx]
        #fy is saying after X-blahblah go up to fx
        fz = float(fy) + fz
        #make sure to give fz a value otherwise it will be undefined
        c = c + 1
        #for every iteration count
    else:
        continue
f = fz / c
print('Average spam confidence:', f)
