from math import ceil
t = int(raw_input())
for _ in xrange(t):
	p,s = map(int,raw_input().split())
	y = (p - (p**2 - 24*s)**0.5)/12
	x = p/4 - 2*y
	print ceil((x*y*y*100))/100