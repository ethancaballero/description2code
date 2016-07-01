from math import*

def check(a):
	if(a==4 or a==7):
		return 1
	a=list(str(a))
	i=0;n=len(a)
	while(i<n):
		if(a[i]=='4' or a[i]=='7'):
			return 1
		i+=1
	return 0

t=input()
while(t):
	t-=1
	n=input()
	i=1;sqr=int(sqrt(n))
	count=0
	while(i<=sqr):
		if(n%i==0):
			count+=check(i)+check(n/i)
		i+=1
	print count