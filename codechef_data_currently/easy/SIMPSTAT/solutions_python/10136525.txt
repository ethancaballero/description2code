# Simple Statistics
# Problem code: SIMPSTAT
# https://www.codechef.com/problems/SIMPSTAT

t=int(raw_input())
for i in range(t):
	n,k=map(int,raw_input().split())
	a=[]
	f=float(0)
	s=float(0)
	a=map(int,raw_input().split())
	a.sort()
	e=int(n-k)
	for i in range(k,e):
		s=s+a[i]
	e=n-(2*k)
	f=s/e
	print '%.6f'%(f)