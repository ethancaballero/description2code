# Splitting Candies
# Problem code: SPCANDY
# https://www.codechef.com/problems/SPCANDY

t=int(raw_input())
for i in range(t):
	n,k=map(int,raw_input().split())
	s=int(0)
	r=int(0)
	if k!=0:
		s=int(n/k)
		r=int(n-(s*k))
	else:
		r=n
	print "%d %d"%(s,r)