testCases = int(raw_input())
for testCase in range(testCases):
	originalString = raw_input()
	lenOfOriginalString = len(originalString)
	# count variables to find the difference between the new string and original one
	count1 = 0 # for "-+-+-+...."
	count2 = 0 # for "+-+-+-...."
	for pos in range(lenOfOriginalString):
		if (pos%2==0):
			# checking >> if char at pos = 0, 2, 4.. is "+" then count1 increased and vice-a-versa
			if (originalString[pos] == "+"):
				count1 += 1
			else: #(originalString[pos] == "-")
				count2 += 1
		else:
			# checking >> if char at pos = 1, 3, 5.. is "-" then count1 increased and vice-a-versa
			if (originalString[pos] == "-"):
				count1 += 1
			else: #(originalString[pos] == "+")
				count2 += 1
	# print the minimum 
	print min(count1,count2)