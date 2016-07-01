t= input()
while(t>0):
	t-=1
	L=[0]*101;i=0
	n,m=map(int,raw_input().split())
	while(i<n):
		p,l=map(int,raw_input().split())
		L[l]+=p
		i+=1
	i=0
	while(i<m):
		p,l=map(int,raw_input().split())
		L[l]-=p
		i+=1
	i=1;p=0
	while(i<101):
		#print i
		if(L[i]<0):
			p-=L[i]
		i+=1
	print p