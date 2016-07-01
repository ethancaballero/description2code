#!/usr/bin/python
from sys import stdin

T = int(stdin.readline())
global N,K,M,R
global minimal

def check(i,current):
    global N,K,M,R
    global minimal
    #print current,minimal,i,R
    if current >= minimal:
        return
    if i >= N:
        if current < minimal:
            minimal = current
        return


    #print current,R
    for add in [0,1]:
        R[i] += add

        if i >= K - 1:
            start = 1 + min(i - K, N - K)
            end   = start + K
            #print start, end
            high = R[start]
            start += 1
            count = 1
            while start < end:
                if R[start] == high:
                    count += 1
                elif R[start] > high:
                    high = R[start]
                    count = 1
                start += 1
        else:
            count = 0
        if count < M:
            check(i+1, current + add)
            if minimal == 0:return
        R[i] -= add

#T = 1
for _ in xrange(T):
    N,K,M = (int(x) for x in stdin.readline().split())
    R = [int(x) for x in stdin.readline().split()]
    current = 0
    minimal = N+1
    if M == 0:
        minimal = 0
    elif M != 1:
        check(0,0)
    if minimal == N+1:
        print '-1'
    else:
        print minimal

