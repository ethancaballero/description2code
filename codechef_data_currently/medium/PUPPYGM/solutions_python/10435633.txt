t=input()
while(t>0):
	t-=1
	a,b=map(int,raw_input().split())
	if(a%2!=0 and b%2!=0):
		print "Vanka"
	else:
		print "Tuzik"