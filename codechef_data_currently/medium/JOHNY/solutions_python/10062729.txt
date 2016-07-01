for i in range(input()):
	n = input()
	a= map(int,raw_input().split())
	c=a[input()-1]
	a=sorted(a)
	while(n>0):
		if(a[n-1]==c):
			print n
			break
		n-=1
