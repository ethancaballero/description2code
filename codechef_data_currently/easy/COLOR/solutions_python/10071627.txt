#!/usr/bin/env python

testcases = int(raw_input())
if(testcases<1 or testcases>10):
    exit()
for i in range(0, testcases):
    N = int(raw_input())
    if(N<1 or N>pow(10,5)):
    	exit()
    S=raw_input()
    noR=S.count("R")
    noG=S.count("G")
    noB=S.count("B")
    ans=len(S)-max(noR,noG,noB)
    print ans


