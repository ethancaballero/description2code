'''import math


tc=input()
for i in xrange(tc):
	a,b = map(int,raw_input().split())
	
	y=math.sqrt(abs(a*a - b*b))
	x=math.sqrt(a*a + b*b)
	
	
	print x,y'''

t = input()
for _ in xrange(t):
    a, b = map(int, raw_input().split())
    print (b * b - a * a) ** 0.5, (b * b + a * a) ** 0.5
 
