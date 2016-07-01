t=input()
while(t>0):
	t-=1
	n=input()
	arr=map(int,raw_input().split())
	index=0
	count=0
	while(index<n):
		if(index==0):
			if(arr[index+1]!=arr[0]):
				count+=1
		elif(index>=1 and index<n-1):
			if(arr[index]!=arr[index+1] or arr[index]!=arr[index-1]):
				count+=1
		else:
			if(arr[index]!=arr[index-1]):
				count+=1
		index+=1
	print count