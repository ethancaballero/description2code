t = input()
while(t>0):
	t-=1
	r = input()
	a=map(int,raw_input().split())
	b=map(int,raw_input().split())
	c=map(int,raw_input().split())
	count=0
	if( (a[0]-b[0])**2 +(a[1]-b[1])**2 <=r**2 ):
		count+=1
	if( (b[0]-c[0])**2 +(c[1]-b[1])**2 <=r**2):
		count+=1
	if( (c[0]-a[0])**2 +(c[1]-a[1])**2 <=r**2):
		count+=1
	if(count>=2):
		print "yes"
	else:
		print "no"