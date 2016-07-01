t=input()
while(t>0):
	t-=1
	n=input()
	N= 103993;R=33102;index=0;s="3."
#	print "r"
	r=N%R
#	print r
	while(index<n):
	#	print "while"
	#	print "index"
		index+=1
	#	print index
		r=r*10
		while(r<R and index<n):
		#	print "while-while"
			r=r*10
			s=s+str(0)
			index+=1
#		p#rint "r"
		#print r
		s=s+str(r/R)
		r=r%R
#		print "s"
#		print s
#		print "r"
#		print r
	if(n==0):print 3
	else: print s
