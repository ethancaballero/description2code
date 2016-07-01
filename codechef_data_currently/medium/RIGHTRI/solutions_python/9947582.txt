t = int(raw_input())
ans = 0
for i in xrange(t):
	x1,y1,x2,y2,x3,y3 = map(int,raw_input().split())
	a = (x1-x2)**2 + (y1-y2)**2
	b = (x2-x3)**2 + (y2-y3)**2
	c = (x3-x1)**2 + (y3-y1)**2
	if (a+b+c)/2 == max(a,b,c):
		ans += 1
print ans