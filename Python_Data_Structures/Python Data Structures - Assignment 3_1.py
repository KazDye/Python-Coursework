hrs = input("Enter Hours:")
rate = input ("Enter Rate:")
try:
    h = float(hrs)
    r = float(rate)
except:
    print("error enter numeric value")
    quit()
if h > 40 :
    x = (h - 40) * (r * 1.5) + (40 * r)
else:
    x = h * r
print(x)
