
t=input()
while(t):
	t-=1
	n=input()
	arrn=map(int,raw_input().split())
	i=0;mini=99999999999
	while(i<n-1):
		while(arrn[i]!=arrn[i+1]):
			if(arrn[i+1]>arrn[i]):
				arrn[i+1]=arrn[i+1]%arrn[i]
				if(arrn[i+1]==0):
					arrn[i+1]=arrn[i]
			else:
				arrn[i]=arrn[i]%arrn[i+1]
				if(arrn[i]==0):
					arrn[i]=arrn[i+1]
			#print arrn
		if(mini>arrn[i+1]):
			mini=arrn[i+1]
		i+=1
	print mini