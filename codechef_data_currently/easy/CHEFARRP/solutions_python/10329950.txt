t=input()
while(t>0):
	t-=1
	n = input()
	arr = map(int,raw_input().split())
	count = 0
	low =0
	high = n-1
	key = 0
	while(high>=low):
		while(high>=key):
			sum1=sum(arr[low:key+1])
			prod = 1
			for i in range(low,key+1):
				prod*=arr[i]
			if(sum1==prod):
				count+=1
			key+=1
		low = low+1
		key=low
	print count