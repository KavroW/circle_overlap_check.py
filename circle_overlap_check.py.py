x1 = float(input("Enter circle1's center x coordinate: "))
y1 = float(input("Enter circle1's center y-coordinates: "))
r1 = float(input("Enter circle1's radius: "))
x2 = float(input("Enter circle2's center x coordinate: "))
y2 = float(input("Enter circle2's center y-coordinates: "))
r2 = float(input("Enter circle2's radius: "))

d = (((x2-x1)**2) + ((y2 - y1)**2))**.5

if d + r2 <= r1:
    print('Circle 2 is inside circle 1')
elif d <= r1 + r2:
    print('Circle 2 overlaps circle 1')
else:
    print('Circle 2 does not overlap circle 1')

