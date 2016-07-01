def luckytest(test,arrl):
	#print "entered"
	#print test
	n=len(test)
	#print "n-m"
	m=len(arrl)
	#print ("%d %d")%(n,m)
	p=False
	i=0;arrt=list(test)
	while(i<m):
		#print "while"
#		print "i"
#		print i
		iter1=len(arrl[i])
		j=0
#		print "iter"
#		print iter1
		while(j+iter1<n+1):
#			print "while-2"
			s=''.join(arrt[j:j+iter1])
#			print "s"
#			print s
			if(s==arrl[i]):
#				print "while-2-if"
				p=True
				return p
			j+=1
		i+=1
	return p

k,n=map(int,raw_input().split())
i=0;arrl=[0]*k
while(i<k):
	arrl[i]=raw_input()
	i+=1
i=0;arrn=[0]*n
#print "arrl"
#print arrl
while(i<n):
	arrn[i]=raw_input()
	i+=1
#print "arrn"
#print arrn
i=0
while(i<n):
	#print "while"
	if(len(arrn[i])>=47):
		print "Good"
	else:
		#print "while-if"
		if( luckytest(arrn[i] , arrl) ):print "Good"
		else: print "Bad"
	i+=1
