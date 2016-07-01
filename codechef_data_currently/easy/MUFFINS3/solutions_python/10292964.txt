t = input()
while(t>0):
	t-=1
	n = input()
	if( n<=2 ):
		print n
	else:
		if( n%2==0 ):
			print n/2+1
		else:
			print (n+1)/2
