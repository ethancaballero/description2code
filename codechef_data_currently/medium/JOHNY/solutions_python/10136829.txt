# Uncle Johny
# Problem code: JOHNY
# https://www.codechef.com/problems/JOHNY

t=int(raw_input())
for i in range(t):
	n=int(raw_input())
	a=[]
	a=map(int,raw_input().split())
	k=int(raw_input())
	s=a[k-1]
	st=int(0)
	a.sort()
	if a[n/2]>=s:
		e=(n/2)
	else:
		st=(n/2)
		e=n-1
	for j in range(0,(e+1-st)):
		if a[j+st]==s:
			break
	print (j+st+1)