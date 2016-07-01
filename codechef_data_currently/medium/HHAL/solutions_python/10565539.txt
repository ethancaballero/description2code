t=input()
while(t>0):
	t-=1
	arr=list(raw_input())
	n=len(arr);p=True
	if(n%2==0):
		for i in range(n/2):
			if(arr[i]!=arr[n-1-i]):
				p=False
	else:
		for i in range((n-1)/2):
			if(arr[i]!=arr[n-1-i]):
				p=False
	if(p):
		print 1
	else:
		print 2