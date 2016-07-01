import math

t = raw_input()
t = int(t)
for i in range(0,t):
	tr = raw_input()
	tr = tr.split()
	tr = map(int,tr)
	m = tr[0]
	n = tr[1]
	k = tr[2]

	if((n == 1 and m == 2) or (n == 2 and m == 1) or (n == 1 and m == 1)):
		print "0"
	elif(m == 1 or n == 1):
		print k
	else:
		print int(math.ceil(k/float(2)))
