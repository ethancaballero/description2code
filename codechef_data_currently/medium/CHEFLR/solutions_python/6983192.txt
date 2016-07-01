t = raw_input()
t = int(t)

for i in range(0,t):
	start = 1
	mystr = raw_input()
	#print mystr
	for j in range(len(mystr)):
		count = j+1
		if(mystr[j] == 'l'):
			if(count%2 == 0):
				start = 2*start - 1
			else:
				start = start*2 
		if(mystr[j] == 'r'):		
			if(count%2 == 0):
				start = start*2 + 1
			else:
				start = start*2 + 2
	print start % 1000000007
