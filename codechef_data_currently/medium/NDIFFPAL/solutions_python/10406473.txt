t = input()
while(t>0):
	t-=1
	n=input()
	a=['a','b','c']
	s=''
	while(n!=0):
		s+=a[n%3]
		n-=1
	print s