t = input()
while(t>0):
	t-=1
	u = input()
	while(u>0):
		u-=1
		k,n,q=map(int,raw_input().split())
		if(n%2!=0):
			if(k==q):
				print (n-1)/2
			else:
				print (n-1)/2+1
		else:
			print n/2