def knapsack(weights,values,maxw):
    n=len(weights)
    m=[]
    tmp=[]
    for i in xrange(0,maxw+1):
	tmp.append(0)
    m.append(tmp)
    for i in xrange(1,n):
	tmp=[]
	for j in xrange(0,maxw+1):
	    if j<weights[i]:
		tmp.append(m[i-1][j])
	    else:
		tmp.append(max(m[i-1][j],m[i-1][j-weights[i]]+p[i]))
	m.append(tmp)
    return m[n-1][maxw]
    
t=int(raw_input())
while t:
    nw=map(int,raw_input().split())
    n=nw[0]
    w=nw[1]
    p=[-1]
    tt=[-1]
    for i in xrange(0,n):
	tr=map(int,raw_input().split())
	p.append(tr[1]*tr[0])
	tt.append(tr[2])
    print knapsack(tt,p,w)
    t-=1