for _ in xrange(int(raw_input())):
    s=raw_input()
    d={}
    n=int(raw_input())
    for i in xrange(n):
        a,b=map(int,raw_input().split())
        if a not in d:
            d[a]=[b]
        else:
            d[a].append(b)
    c,last=0,None
    for i in sorted(d.keys()):
        for j in sorted(d[i],reverse=True):
            if last:
                c+=((last[0]-i)**2+(last[1]-j)**2)**0.5
            last=(i,j)
    print "%0.2f" %c
