t=input()
while(t>0):
	t-=1
	n=input()
	a=[0]*n;c=[0]*n;i=0
	while(i<n):
		b=raw_input().split()
		a[i]=b[0];c[i]=b[2:]
		i+=1
	print "Begin on",
	for j in c[n-1]:
		print j,
	print
	i=n-2
	while(i>=0):
		if(a[i+1]=='Left'):
			print "Right on",
			for j in c[i]:
				print j,
			print
		elif(a[i+1]=='Right'):
			print "Left on",
			for j in c[i]:
				print j,
			print			
		i-=1