t = input()
while(t>0):
	t-=1
	n = input()
	ar = list(raw_input())
	ind=0
	not_ind=0
	for i in ar:
		if( i=='I' ):
			ind+=1
		elif(i=='Y'):
			not_ind+=1
	if(ind>not_ind):
		print "INDIAN"
	elif(not_ind>ind):
		print "NOT INDIAN"
	else:
		print "NOT SURE"