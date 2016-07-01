def freq(arr):
	char=[0]*26;index=0
	count=0
	n=len(arr)
	while(index<n):
		i=(ord(arr[index])-96)%26
		char[i]+=1
		if(char[i]>1):
			count+=1
		index+=1
	return n-count

t= input()
while(t>0):
	t-=1
	arr=list(raw_input())
	print freq(arr)