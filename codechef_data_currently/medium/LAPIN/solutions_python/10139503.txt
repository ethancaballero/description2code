# Lapindromes
# Problem code: LAPIN
# https://www.codechef.com/problems/LAPIN

t=int(raw_input())
for i in range(t):
	s=raw_input()
	l=len(s)
	a=[]
	b=[]
	for j in range(l/2):
		a=a+[ord(s[j])]
		b=b+[ord(s[l-j-1])]
	a.sort()
	b.sort()
	if a==b:
		print("YES")
	else:
		print("NO")




