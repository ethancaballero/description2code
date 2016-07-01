#!/usr/bin/env python

import sys

parent = None
#child = dict()

def find_set(x):
    global parent
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return parent[x]

T = int(sys.stdin.readline())    

while T > 0:
    
    N = int(sys.stdin.readline())
    S = map(int, sys.stdin.readline().strip().split())
    parent = range(1,N + 1)
    
    parent = [-1] + parent
    S = [-1] + S

    q = int(sys.stdin.readline())
    while q > 0:
        q -= 1
        d = map(int, sys.stdin.readline().strip().split())
        k = len(d)
        if k == 3:
            l, m = find_set(d[1]), find_set(d[2])
            if l == m:
                print "Invalid query!"
            elif S[l] > S[m]:
                parent[m] = l
            elif S[l] < S[m]:
                parent[l] = m
        else:
            print find_set(d[1])
    T = T - 1
