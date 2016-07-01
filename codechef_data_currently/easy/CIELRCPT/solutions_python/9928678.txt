import math

tc=int(raw_input())

for i in range(0, tc):
	p=int(raw_input())
	i=11
	count=0
	while(i>=0):
		a=math.pow(2,i)
		count+=int(p/a)
		p=p%a
		i-=1
	print count	

