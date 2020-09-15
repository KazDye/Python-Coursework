fname = input('Enter file name:')
fh = open(fname)
try:
    fh = open(fname)
except:
	print('file cannot be read', fname)
	Quit()
for x in fh :
    try:
        x = x.rstrip()
        print(x.upper())
    except:
        print('error: please use text files only')
        quit()
