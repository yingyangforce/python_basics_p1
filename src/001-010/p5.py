#--------------------------------------------------------
# | p5 - | take user first/last name, print in rev order
#--------------------------------------------------------

import sys

if len(sys.argv) > 1:
    try:
        print(f"Your last, first name is {sys.argv[2]}, {sys.argv[1]}.")
    except:
        print("Err. CLI args should only be first, last name delimed by a space.\n")
else:
    namearr = input("Enter your first and last name: ").split()
    print(f"Your last, first name is {namearr[1]}, {namearr[0]}.")

