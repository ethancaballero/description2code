t =input()
while(t>0):
	t-=1
	m,x,y = map(int,raw_input().split())
	cop_house = [1]*(m+2)
	cop_house[m+1]=100
	cop_house[1:m+1] = map(int,raw_input().split())
	cop_house = sorted(cop_house)
	diff_arr=[0]*(m+1)
	cop_speed = x*y 
#	print "cop_speed"
#	print cop_speed
	count = 0
	for i in range(m+1):
	#	print "i"
	#	print i
		if( i==0 or i==m ):
			diff_arr[i]=cop_house[i+1]-cop_house[i]
	#		print "safe_houses-if"
			safe_houses = diff_arr[i] - cop_speed
	#		print safe_houses
			if(safe_houses >0 ):
				count+= safe_houses
		else:
			diff_arr[i]=cop_house[i+1]-cop_house[i]-1
	#		print "safe_houses-else"
			safe_houses = diff_arr[i]- 2*cop_speed
	#		print safe_houses
			if( safe_houses>0 ):
				count+= safe_houses
	#	print "diff_arr"
	#	print diff_arr[i]
	print count