t= input()
while(t>0):
	t-=1
	a=list(raw_input())
	n=len(a)
	ins=1+n
	for i in range(n-1):
		diff= ord(a[i])-ord(a[i+1])
		if(diff>0):
			ins += 26 - diff
		else:
			ins-=diff
	
	if(n*11>=ins):
		print "YES"
	else:
		print "NO"