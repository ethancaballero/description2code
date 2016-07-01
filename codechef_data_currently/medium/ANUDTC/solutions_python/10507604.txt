t=input()
while(t>0):
	t-=1
	n=input()
	if(360%n==0):
		print "y",
	else:
		print "n",
	if(n<=360):
		print "y",
	else:
		print "n",
	if(n*(n+1)<=720):
		print "y",
	else:
		print "n",
