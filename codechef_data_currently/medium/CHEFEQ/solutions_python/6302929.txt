from sys import stdin
from collections import Counter


for i, ln in enumerate(stdin):
    if i:
        if i % 2 == 1:
            n = int(ln)
        else:
            c = max(Counter(map(int, ln.split())).values())
            print n - c
