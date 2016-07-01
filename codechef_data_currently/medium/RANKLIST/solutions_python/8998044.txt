t = input()

it = 0 
while (it < t):
	s = raw_input()
	s1 = s.split(" ")
	n = int(s1[0])
	s = int(s1[1])
	#print n, s 
	if (s == (n*(n+1))/2):
		print "0" 
		it += 1
		continue
	s -= n 
	for i in range(1,n):
		if ((s < ((n-i)*(n-i+1))/2) & (s >= ((n-i-1)*(n-i))/2) ):
			print i 
			break

	it += 1 