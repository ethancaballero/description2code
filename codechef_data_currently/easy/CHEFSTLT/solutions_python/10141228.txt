# Chef and Two Strings
# Problem code: CHEFSTLT
# https://www.codechef.com/problems/CHEFSTLT

t=int(raw_input())
for i in range(t):
	a=raw_input()
	b=raw_input()
	l=len(a)
	ma=int(0)
	mi=int(0)
	for j in range(l):
		if a[j]!=b[j] and a[j]!='?' and b[j]!='?':
			mi=mi+1
			ma=ma+1
		elif a[j]=='?' and b[j]=='?':
			ma=ma+1
		elif (a[j]=='?' or b[j]=='?') and (a[j]!=b[j]):
			ma=ma+1
	print'%d %d'%(mi,ma)
