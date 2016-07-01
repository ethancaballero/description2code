t=input()
while(t>0):
	t-=1
	n=input()
	arr=map(int,raw_input().split())
	count=[0]*100001;i=0;counter=0
	while(i<n):
		if(count[arr[i]]==0):
			count[arr[i]]=1
			counter+=1
		i+=1
	print counter