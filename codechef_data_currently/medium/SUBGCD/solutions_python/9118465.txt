from fractions import gcd

t = input()
for _ in xrange(t):
	n = input()
	l = list(map(int,raw_input().split()))
	g = l[0]
	for i in l:
		g = gcd(g,i)
		if(g==1): break
	if(g==1): print n
	else: print -1
