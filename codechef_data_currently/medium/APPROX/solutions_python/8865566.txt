t = input()
for i in range(t):
	k = input()
	if k<=0:
		arr = ["3"]
	else:
		arr = ["3" , "."]
	rem = 103993%33102
	for j in range(1,k+1):
		rem *= 10
		arr.append(str(rem/33102))
		rem %= 33102
	print "".join(arr)

	