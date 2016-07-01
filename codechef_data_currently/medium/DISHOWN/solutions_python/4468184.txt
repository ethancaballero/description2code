#!/usr/bin/env python

import sys

def find_set(P,d):
    while P[d] != d:
        P[d] = P[P[d]]
        d = P[d]
    return P[d]

T = int(sys.stdin.readline())    

while T > 0:
    
    N = int(sys.stdin.readline())
    S = map(int, sys.stdin.readline().strip().split())
    P = range(1,N + 1)
    
    P = [-1] + P
    S = [-1] + S

    Q = int(sys.stdin.readline())

    while Q > 0:
        d = map(int, sys.stdin.readline().strip().split())
        k = len(d)
        if k == 3:
            cx, cy = find_set(P,d[1]), find_set(P,d[2])
            if cx == cy:
                print "Invalid query!"
            elif S[cx] > S[cy]:
                P[cy] = cx
            elif S[cx] < S[cy]:
                P[cx] = cy
        else:
            print find_set(P,d[1])
        Q = Q - 1

    T = T - 1
