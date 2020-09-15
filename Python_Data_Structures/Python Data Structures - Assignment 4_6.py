hrs = input("Enter Hours:")
rte = input("Enter Rate:")
try:
    h = float(hrs)
except:
    print("Error: Please Enter Numeric Value")
    quit()
try:
    r = float(rte)
except:
    print("Error: Please Enter Numeric Value")
    quit()
if h > 40:
    def computepay(h,r):
        return (h - 40) * (r * 1.5) + (40 * r)
else:
    def computepay(h,r):
        return h * r
x = computepay(h, r)
print(x)
