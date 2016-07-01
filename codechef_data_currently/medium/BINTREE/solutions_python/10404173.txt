'''def classifeir(a):
	while(a[0]/2!=1):
		a[0]=a[0]/2
	while(a[1]/2!=1):
		a[1]=a[1]/2
	if(a[0]==a[1]):
		return True
	else:
		return False


t = input()
while(t>0):
	t-=1
	arr=map(int,raw_input().split())
	count=[0]*2
	index=0
	sum1=0
	p=classifeir(arr[:])
	print p
	if(arr[1]!=arr[0]):
		if(arr[0]%2==0 and arr[1]==arr[0]+1 or arr[1]%2==0 and arr[0]==arr[1]+1 ):
			sum1=2
		else:
			while(index<2):
				while(arr[index]!=1):
					if(arr[index]%2==0):
						arr[index]=arr[index]/2
						count[index]+=1
					else:
						arr[index]=(arr[index]-1)/2
						count[index]+=1
				index+=1
			if(p):
				sum1=abs(count[0]-count[1])
			else:
				sum1=count[0]+count[1]
	print sum1'''


t= input()
while(t>0):
	t-=1
	i,j=map(int,raw_input().split())
	count=0
	while(i!=j):
		if(i>j):
			i=i/2
			count+=1
		else:
			j=j/2
			count+=1
	print count
