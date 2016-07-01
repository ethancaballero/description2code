t = input()
a = [100,50,10,5,2,1]
while(t>0):
	t-=1
	n = input()
	count = 0
	for i in a:
		p = True
		while(p):
			if(n-i>=0):
				n=n-i
				count+=1
			else:
				p = False
	print count