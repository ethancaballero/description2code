# Minimum Maximum
# Problem code: MNMX
# https://www.codechef.com/problems/MNMX

t=int(raw_input())
for i in range(t):
	n=int(raw_input())
	a=[]
	a=map(int,raw_input().split())
	a.sort()
	l=len(a)
	s=a[0]
	s=s*(l-1)
	print s