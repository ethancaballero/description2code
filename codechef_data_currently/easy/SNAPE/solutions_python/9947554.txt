t = int(raw_input())
for i in xrange(t):
	b,ls = map(int,raw_input().split())
	minrs = (ls**2 - b**2)**0.5
	maxrs = (ls**2 + b**2)**0.5
	print minrs,maxrs