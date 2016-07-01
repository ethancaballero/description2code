for i in range(input()):
	a=list(raw_input())
	b=[0]*200
	n=len(a)
	m=0
	if(n%2!=0):
		while(m<(n-1)/2):
			b[ord(a[m])]+=1
			b[ord(a[n-m-1])]+=1
			m+=1
	else:
		while(m<n/2):
			b[ord(a[m])]+=1
			b[ord(a[n-m-1])]+=1
			m+=1
	m=97
	while(m<123):
		if(b[m]%2!=0):
			print "NO"
			break
		elif(m==122):
			print "YES"
		m+=1