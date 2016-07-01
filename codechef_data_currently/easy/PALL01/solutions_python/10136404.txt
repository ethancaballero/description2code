# The Block Game
# Problem code: PALL01
# https://www.codechef.com/problems/PALL01

t=int(raw_input())
for i in range(t):
	a=int(raw_input())
	rev=a
	b=int(0)
	while a!=0:
		b=(b*10)+(a%10)
		a=a/10
	if b==rev:
		print("wins")
	else:
		print("losses")
