t=input()
while(t>0):
	n,k,e,m=map(int,raw_input().split())
	s=[]
	i=0
	while(i<n-1):
		a=map(int,raw_input().split())
		s.append(sum(a))
		i+=1
	a=map(int,raw_input().split())
	a=sum(a)
	#print "s"
	s.append(a);i=0;e=0
	while(i<n-1):
		if(s[i]>=a):e+=1
		i+=1
	#print s
	s=sorted(s,reverse=True)
	#print s
	#print "e"
	#print e
	if(e<=k-1):
		print 0
	else:
		#print "diff"
		diff=s[k-1]-a
		#print diff
		if(diff>=m):
			print "Impossible"
		else:
			print diff+1
	t-=1