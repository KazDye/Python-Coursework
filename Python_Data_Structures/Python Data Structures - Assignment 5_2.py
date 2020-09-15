#largest = None
#smallest = None
#while True:
#    num = input("Enter a number:")
#    if num == "done": break
#    try:
#        fnum=float(num)
#        if smallest is None:
#            smallest = fnum
#        elif fnum < smallest:
#            smallest = fnum
#        if largest is None:
#            largest = fnum
#        elif fnum > largest:
#            largest = fnum
#        sm=int(smallest)
#        lg=int(largest)
#    except:
#        print('Invalid input')
#        continue
#print('Maximum is', lg)
#print('Minimum is', sm)

largest = None
smallest = None
while True:
    num = input("Enter a number:")
    if num == "done": break
    try:
        fnum=int(num)
        if smallest is None:
            smallest = fnum
        elif fnum < smallest:
            smallest = fnum
        if largest is None:
            largest = fnum
        elif fnum > largest:
            largest = fnum
    except:
        print('Invalid input')
        continue
print('Maximum is', largest)
print('Minimum is', smallest)
