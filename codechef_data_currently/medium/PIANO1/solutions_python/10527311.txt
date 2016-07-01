t=input()
while(t>0):
	t-=1
	arr=list(raw_input())
	n=input()
	l=len(arr);i=0;fact=0
	while(i<l):
		if(arr[i]=='T'):
			fact+=2
		else:
			fact+=1
		i+=1
	#print fact
	i=1;l=0;count=0;iter1=(12*n)/fact
	while(i<=iter1):
		l = 12*n-fact*i
		#print l
		if(l>=1):
			count+=l
		i+=1
	print count