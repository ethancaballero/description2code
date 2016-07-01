# Input for number of tests
t = int(input())

for n in range(t):
	
	# Various inputs
	n_q = int(input()) 
	corAns = raw_input()
	chefAns = raw_input()
	p = raw_input().strip().split(" ")

	for x in range(0, len(p)):
		p[x] = int(p[x])

	# Checking which of chef's answers are correct
	noCor = 0
	for x in range(0, n_q):
		if corAns[x] == chefAns[x]:
			noCor += 1

	if noCor == n_q:
		
		finalPoints = p[noCor]
	
	else:
	
		# Checking what is the highest score possible
		grtstNo = 0
		grtstNoElmnt = 0
		for x in range(0, noCor+1):
			if p[x] > grtstNo:
				grtstNo = p[x]
				grtstNoElmnt = x

		# Calculating the final number of points earned
		finalPoints = p[grtstNoElmnt]

	print(finalPoints)



	
		

