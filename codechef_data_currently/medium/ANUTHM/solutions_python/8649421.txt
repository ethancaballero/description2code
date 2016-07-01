t=int(raw_input())

while(t>0):
    t-=1
    n,m=[int(i) for i in raw_input().split()]
    print ("%.6f" % (n+m-1))