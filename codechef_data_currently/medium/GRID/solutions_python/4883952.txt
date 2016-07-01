def proc(a):
    n=len(a)
    j=n-1
    l=0
    ans=0
    hsh=[True]*n
    for j in range(n-1,-1,-1):
        i=n-1
        flag=True
        while i>=0:
            if a[i][j]=='#':
                hsh[i]=False
                flag=False
            elif hsh[i] and flag: ans+=1
            i-=1
    print ans
t=int(input())
for ii in range(t):
    n=int(input())
    a=[ raw_input() for i in range(n)]
    proc(a)
