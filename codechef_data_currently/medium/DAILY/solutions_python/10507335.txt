def permute(count,per):
	num=1;din=1
	while(per>0):
		num*=count
		din*=per
		per-=1
		count-=1
	return num/din

x,n=map(int,raw_input().split())
poss=0
while(n>0):
	count=map(int,list(raw_input()))
	s=[0]*55;s[1:]=count
	#print s
	n-=1
	i=1;j=54
	while(i<34):
		while(j>27):
			'''print "i-j"
			print ("%d %d ")%(i,j)'''
			count=[0]*2
			count[s[i]]+=1
			count[s[i+1]]+=1
			count[s[i+2]]+=1
			count[s[i+3]]+=1
			count[s[j]]+=1
			count[s[j-1]]+=1
			'''print 
			print s[i]
			print s[i+1]
			print s[i+2]
			print s[i+3]
			print s[j]
			print s[j-1]
			print'''
			break
		i+=4
		j-=2
		if(count[0]>=x):
			poss+=permute(count[0],x)
		#print "poss"
		#print poss
print poss