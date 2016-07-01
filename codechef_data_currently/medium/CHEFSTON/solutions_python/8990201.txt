t = input()

j = 0 
while (j < t ) : 
	s = raw_input()
	s1 = s.split(" ")
	n = int(s1[0])
	k = int(s1[1]) 
	a = []
	s = raw_input()
	s1 = s.split(" ")

	for i in range(n):
		a.append(int(s1[i]))
	s = raw_input()
	s1 = s.split(" ")
	b = []
	for i in range(n):
		b.append(int(s1[i]))

	maxi = -1 
	for i in range(n):
		if (maxi < (k/a[i] )*b[i]) : 
			maxi = (k/a[i])*b[i] 
	print maxi 

	j += 1 