import sys
from collections import Counter
 
t = sys.stdin.readline()
m = 1
M = 1000000000
for _ in range(int(t)):
	k = sys.stdin.readline()
	k = int(k)
	assert(1 <= k <= 100000)
	c = Counter()
	for _ in range(k):
		line = sys.stdin.readline()
		o, l, v = line.strip().split()
		l = int(l)
		assert(m <= l <= M)
		v = v.upper()
		if o == '<' and v == 'YES': #less
			c[l] += 1				
		elif o == '<' and v == 'NO': #great or equal 
			c[m] += 1				 
			c[l] -= 1
		elif o == '>' and v == 'YES':	#great
			c[m] += 1
			c[l+1] -= 1
		elif o == '>' and v == 'NO':	#less or equal
			c[l+1] += 1
		elif o == '=' and v == 'YES':
			c[m] += 1
			c[l] -= 1
			c[l+1] += 1
		elif o == '=' and v == 'NO':
			c[l] += 1
			c[l+1] -= 1
 
	count = 0
	mcount = k
	for key in sorted(c):
		count += c[key]
		if key <= M:
			mcount = min(mcount, count)
	print(mcount)