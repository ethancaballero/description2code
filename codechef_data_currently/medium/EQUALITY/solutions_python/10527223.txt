t=input()
while(t>0):
	n=input()
	arr=map(int,raw_input().split())
	s=sum(arr);j=0;sol=[]
	while(j<n):
		sol.append(s/(n-1)-arr[j])
		j+=1
	j=0;#sol=sorted(sol)
	while(j<n):
		print ("%d")%(sol[j]),
		j+=1
	t-=1
