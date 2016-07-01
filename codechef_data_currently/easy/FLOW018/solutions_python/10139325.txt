# Small Factorial
# Problem code: FLOW018
# https://www.codechef.com/problems/FLOW018

def fact(n):
	if n==0:
		return 1
	else:
		return n*fact(n-1)

t=int(raw_input())
for i in range(t):
	n=int(raw_input())
	print fact(n)

