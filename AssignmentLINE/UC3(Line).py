import math

x1, y1 = 0, 0
x2, y2 = 3, 4

x3, y3 = 0, 0
x4, y4 = 6, 8

len1 = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
len2 = math.sqrt((x4 - x3)**2 + (y4 - y3)**2)

if abs(len1 - len2) < 1 * 10**-9:
    print("Lines are Equal")
elif len1 > len2:
    print("Line 1 is Greater than Line 2")
else:
    print("Line 1 is Less than Line 2")