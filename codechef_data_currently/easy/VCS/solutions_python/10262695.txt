for i in range(input()):
	a,b,c=map(int,raw_input().split())
	count = [0]*(a+1)
	ar1 = map(int,raw_input().split())
	ar2=map(int,raw_input().split())
	for i in ar1:
		count[i]+=1
	for i in ar2:
		count[i]+=1
	trig =0
	untunig = 0
	for i in range(1,a+1):
		if(count[i]==2):
			trig+=1
		if(count[i]==0):
			untunig+=1
	print ("%d %d")%(trig,untunig)