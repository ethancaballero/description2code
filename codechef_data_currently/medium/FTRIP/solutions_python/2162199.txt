global FACT
FACT=[]
FACT.append(1)
for i in range(1,1001):
	FACT.append(i*FACT[i-1])

def nCr(n,r):
	if n<r:
		return 0
	else: 
		return (FACT[n]/FACT[n-r]/FACT[r])
		
t=input()
for _ in range(0,t):
	s,n,m,k=map(int,raw_input().split(' '))
	ans=0
	if k==0:
		print "1.000000"
	elif s==n:
		print "1.000000"
	elif k>=n:
		print "0.000000"
	else:
		if m>n:
			p=n
		else:
			p=m
		for j in range(k,m):
			a=nCr(m-1,j)
			b=nCr(s-m,n-j-1)
			ans+=(a*b)
		print"%.8f"%(ans/float(nCr(s-1,n-1)))
