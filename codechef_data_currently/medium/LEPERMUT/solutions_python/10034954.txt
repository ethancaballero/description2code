t =input()
while(t>0):
	n = input()
	a = map(int, list(raw_input().split()))
	sum = 0 
	for i in range(n-1):
		if( a[i]>a[i+1] ):
			sum+=1
		for j in range(i+1,n):
			if( a[i]>a[j] ):
				sum-=1
	if( sum==0 ):
		print "YES"
	else:
		print "NO"
	t-=1