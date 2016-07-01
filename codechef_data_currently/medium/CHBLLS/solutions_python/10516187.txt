import sys
w=[0]*6
i=1
while(i<6):
	print 1
	print ("1 %d")%(i)
	print 0
	sys.stdout.flush()
	w[i]=int(raw_input().strip())
	i+=1
print 2
print w.index(max(w))