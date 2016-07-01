from sys import stdin


def gcd(a, b):
    while a % b:
        a, b = b, a % b
    return b


for i, ln in enumerate(stdin):
    if i:
        if i % 2 == 1:
            n = int(ln)
        else:
            print n if reduce(gcd, map(int, ln.split())) == 1 else -1
