t = input() 
for i in range(t):
	direction = "Begin"
	n = input()
	str = [""]*(n)
	for j in range(n):
		str[j] = raw_input()
		j += 1
	j = n-1 
	while(j >= 0):
		temp = str[j].split()
		new_direction = temp[0]
		if direction == "Begin":
			temp[0] = "Begin"
		elif direction == "Left":
			temp[0] = "Right" 
		elif direction == "Right":
			temp[0] = "Left"
		direction = new_direction
		j -= 1
		print " ".join(temp)
	print ""