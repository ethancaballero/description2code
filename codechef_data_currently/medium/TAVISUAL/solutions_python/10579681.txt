t=input()
while(t>0):
	t-=1
	n,c,q=map(int,raw_input().split())
	i=0
	while(i<q):
		l,r=map(int,raw_input().split())
		if(l<=c and c<=r):
			ln=r-l+1
			pc=c-l+1
			c=l+ln-pc
		i+=1
	print c