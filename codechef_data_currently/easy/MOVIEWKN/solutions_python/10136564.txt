# Movie Weekend
# Problem code: MOVIEWKN
# https://www.codechef.com/problems/MOVIEWKN

t=int(raw_input())
for i in range(t):
	n=int(raw_input())
	r=[]
	l=[]
	max=int(0)
	ind=int(n)
	rate=int(0)
	l=map(int,raw_input().split())
	r=map(int,raw_input().split())
	for j in range(n):
		if r[j]*l[j]>=max:
			max=r[j]*l[j]
			if r[j]>rate:
			    rate=r[j]
			    ind=j
	print (ind+1)
