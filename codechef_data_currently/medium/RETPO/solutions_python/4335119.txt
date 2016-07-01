import sys

def caseXY(x,y):
    if x == 0:
        if y % 2 == 0:
            return 2 * y
        else:
            return 2 *(y - 1) + 1
    elif y == 0:
        if x % 2 == 0:
            return 2 * x
        else :
            return 2 * x + 1
    else:
        assert x == 0 and y == 0
        return 0

def solve(x,y):
    x = abs(x)
    y = abs(y)

    z = min(x,y)

    return 2 * z + caseXY(x - z, y - z)

T = int( raw_input() ) 

while T > 0:
    l = raw_input()
    ls = l.split()
    x = int( ls[0] )
    y = int( ls[1] )
    print solve(x,y)
    T = T - 1

