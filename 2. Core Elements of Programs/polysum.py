from math import tan, pi

def polysum(n, s):
    """
    Inputs:
        n: an int; no. of sides in the polygon
        s: an int; length of polygon side
    
    polysum() returns the sum of
        a) the area of the polygon
        b) the square of the polygon's perimeter
    """
    area = (0.25*n*s**2)/(tan(pi/n))
    perimeter = n*s
    return round(area + (perimeter)**2, 4)
    