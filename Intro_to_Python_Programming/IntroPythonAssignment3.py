netflix = input("For A Netlix TV Show Recommendation Please Enter A Number Between 1 and 10: ")
try:
    netflix = int(netflix)
except:
    print("Unhandled Exception: Please enter a numeric value between 1 and 10")
    quit()
if netflix == 1:
    x = "'Star Trek: Deep Space Nine'"
elif netflix == 2:
    x = "'Star Trek: The Next Generation'"
elif netflix == 3:
    x = "'The Umbrella Academy'"
elif netflix == 4:
    x = "'Tiger King'"
elif netflix == 5:
    x = "'Community'"
elif netflix == 6:
    x = "'Full Metal Alchemist: Brotherhood'"
elif netflix == 7:
    x = "'Lucifer'"
elif netflix == 8:
    x = "'Altered Carbon'"
elif netflix == 9:
    x = "'Love is Blind'"
elif netflix == 10:
    x = "'Too Hot to Handle'"
else:
    print("Please Choose A Number Between 1 And 10!")
    quit()
print("You Should Watch: " + x + " On Netflix")
