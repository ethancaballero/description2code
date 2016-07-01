t = input()
while(t>0):
	t-=1
	a = map(int,raw_input().split())
	max1=1
	low=0
	while(low<=2):
		if(max1<a[low]):
			max1=a[low]
		low+=1
	low=0
	max2=1
	while(low<=2):
		if(a[low]!=max1 and max2<a[low]):
			max2=a[low]
		low+=1
	print max2