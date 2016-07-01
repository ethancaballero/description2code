t=input()
while(t):
	t-=1
	n=input()
	arrp=map(int,raw_input().split())
	i=0;mini=arrp[0];index=0;sum1=0
	while(i<n):
		sum1+=arrp[i]
		if(mini>arrp[i]):
			mini=arrp[i]
			index=i
		i+=1
	print mini*(sum1-mini)