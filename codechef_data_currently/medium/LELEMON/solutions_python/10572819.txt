t=input()
while(t>0):
	t-=1
	n,m=map(int,raw_input().split())
	pr=map(int,raw_input().split())
	arr=[];r=[]
	i=0
	while(i<n):
		r=map(int,raw_input().split())
		arr.append(r[1:])
		i+=1
	i=0;count=0
	#print arr
	while(i<m):
		n=pr[i]
		arrl=len(arr[n])
		if(arrl>0):
			j=0;r=0
			while(j<arrl):
				if(arr[n][j]>r):
					r=arr[n][j]
				j+=1
			count+=r
			arr[n].remove(r)
		i+=1
	print count