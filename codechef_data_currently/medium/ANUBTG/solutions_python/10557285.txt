t=int(raw_input())
while(t>0):
	t-=1
	n=int(raw_input())
	arr=map(int,raw_input().split())
	arr=sorted(arr,reverse=True);i=0;count=0
	while(i<n):
		count+=arr[i]
		if(i+1<n):
			count+=arr[i+1]
		i+=4
	print count