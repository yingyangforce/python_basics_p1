#-----------------------------------------------------
# | p4 - | get radius from user, print area of circle
#-----------------------------------------------------

import sys, math

if __name__ == '__main__':
    if len(sys.argv) == 2:
        radius = float(sys.argv[1])
        area = math.pi * (radius ** 2)
        print(f"Area of circle for r={radius} -> {area:.3f}")
    


