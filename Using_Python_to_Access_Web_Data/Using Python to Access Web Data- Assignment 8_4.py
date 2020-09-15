a = input('Enter File name:')
b = open(a)
l = list()
for x in b:
    x = x.strip()
    y = x.split()
    for z in y:
        if z not in l:
            l.append(z)
l.sort()
print(l)

#Enter File name
#Open File
#Create Blank list
#For variables in the file
#remove blank spaces and hidden characters
#Turn file into a list
#for the individual points in the list
#If the individual points do not exist in the list
#Add them to the list
#Sort the list
#Print the list
