# Author : Kishor shrestha
#  Write a Python program which accepts the radius of a circle from the user and compute the area. [Note: use string formatter and placeholders to prettify your output. Your output should be only upto 3 dedimal places.]

def calculatearea(radiusofcircle = 0):
    return (22/7)*radiusofcircle*radiusofcircle

inradius = float(input("Enter the radius of circle \n"))
print("\nThe area of the circle with radius {0} is {1:.3f}".format(inradius,calculatearea(inradius)))