p=input()
while(p>0):
	p-=1
	n=input()
	x=[0]*n;l=[0]*n;f=[0]*n;t=[0]*n
	i=0
	while(i<n):
		x[i],l[i],f[i]=map(int,raw_input().split())
		i+=1
	t[0]=x[0]+l[0]
	i=1
	while(i<n):
		if( t[i-1]>x[i] ):
			if((t[i-1]-x[i])%f[i]==0):
				t[i]=l[i]+t[i-1]
			else:
				t[i]=f[i]-(t[i-1]-x[i])%f[i] + l[i]+t[i-1]
		if( t[i-1]<=x[i] ):
			t[i]=x[i]-t[i-1]+l[i]+t[i-1]
		i+=1
	#$print t
	print t[n-1]
