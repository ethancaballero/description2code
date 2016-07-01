from sys import stdin


for i, ln in enumerate(stdin):
    if not i:
        n, _ = map(int, ln.split())
    else:
        k = int(ln)
        if k < n + 1:
            print 0
        elif k > 2 * n:
            print 3 * n - k + 1
        else:
            print k - n - 1
