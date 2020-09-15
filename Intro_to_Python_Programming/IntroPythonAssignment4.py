a = 10000
x = 100
while a >= 0:
    print(a)
    a = a - x
    x -= 1
    if x < 10:
        x = 100

#Comments
#a = 10000

#From the list, 10000 was the initial number in the series
#That was why I made the printed variable "a" start with 10000

#x = 100
#The pattern that I initially saw was that it was decreasing by 100
#That was the why I made the variable "x" 100 to decrease from variable "a"

#while a >= 0:
#The list of numbers ended with 0 so we needed to include the printed result "0" thus >=0
#I also chose while as I believed that the loop was fixed in that it would end after a became 0

    #print(a)
    #This was so we could display the numbers

    #a = a - x
    #This was the initial pattern I recognized
    #This had to come after the print statement otherwise the numbers would start from 9900 and end with -10

    #x -= 1
    #This was the pattern that I thought encompassed the whole series of numbers.
    #I had originally added in if x = 0: break but the numbers ended at 4951.
    #I had also previously omitted to add the "if" portion of code which resulted in an infinite loop.
    #The loop was caused by the negative number for variable "x" began to add to the variable "a".
    #I quickly realized my mistake and corrected it

    #if x < 10:
        #x = 100
    #When I reviewed the list I realized that the numbering scheme changed between 5005, 4995 and 4895.
    #I realized that the pattern reset after x went below 10.
    #I added this after the x -= 1 so it would reset 'x' anytime its value went under 10 for the next loop.
