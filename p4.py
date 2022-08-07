#-----------------------------------------------------
# | p4 - | get radius from user, print area of circle
#-----------------------------------------------------

import sys, math

if __name__ == '__main__':
    if len(sys.argv) > 1:
        radius = float(sys.argv[1])
    else:
        radius = float(input("Enter the radius of your circle: "))

    if radius == int(radius):
        radius = int(radius)

    area = math.pi * (radius ** 2)
    print(f"Area of circle for r={radius} -> {area:.3f}")


