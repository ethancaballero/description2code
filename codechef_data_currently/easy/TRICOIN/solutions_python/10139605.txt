# Coins And Triangle
# Problem code: TRICOIN
# https://www.codechef.com/problems/TRICOIN

t=int(raw_input())
for i in range(t):
	n=int(raw_input())
	s=int(1)
	j=int(2)
	while n>=s:
		s=(j*(j+1))/2
		j=j+1
	print j-2
