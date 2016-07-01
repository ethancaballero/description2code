import sys
t=int(sys.stdin.readline())
while t!=0:
    n=int(sys.stdin.readline())
    s=0
    m=0;
    x=sys.stdin.readline().split()
    for i in range(0,n):
        x[i]=int(x[i])
        if x[i]>m:
            m=x[i]
            s=0
        if x[i]==m:
            s=(s*2+1)%1000000007
    print s
    t-=1
