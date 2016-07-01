for i in range(int(raw_input())):
	bal = 0
	max_bal = 0
	for j in raw_input():
		if j=='(':
			bal = bal + 1
		else:
			bal = bal - 1
		max_bal = max(max_bal,bal)
	print '('*max_bal + ')'*max_bal