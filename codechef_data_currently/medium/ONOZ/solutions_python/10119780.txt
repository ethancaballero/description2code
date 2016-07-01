def identical(i,j):
	#print "i"
	#print i
	#print j
	#print "else"
	i=str(i)+str(j)
	#print "i"
	#print i
	m=0
	n=len(i)
	i=int(i)
	j=i%10
	i=i/10
	#print "j"
	#print j
	#print "i"
	#print i
	while(True):
		#print "while"
		#print "i"
		#print i
		if(i%10!=j and i!=0):
			#print "while-if"
			return 0
		elif(i%10==j and i!=0):
			#print "while-elif-1"
			i=i/10
			m+=1
		elif(i==0):
			#print "while-elif-2"
			break
	if(m==n-1):
		#print "else-if"
		return 1
	else:
		#print "else-else"
		return 0

for k in range(input()):
	#print "1"
	h,m=map(int,raw_input().split())
	#print "result"
	#print h
	#print m
	sum=0
	for i in range(h):
		for j in range(m):
			#print "iden"
			#print identical(i,j)
			sum+=identical(i,j)
			#print "sum"
			#print sum
	#print "result"
	print sum+1