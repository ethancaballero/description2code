# Chef and String
# Problem code: CHRL2
# https://www.codechef.com/problems/CHRL2
import math
s=raw_input()
l=len(s)
c=int(0)
a=int(0)
b=int(0)
d=int(0)
for i in range(l):
	if s[i]=='C':
		a=max(i+1,a)
		while a<l and s[a]!='H':
			a+=1
		if a==l:
			break
		b=max(b,a+1)
		while b<l and s[b]!='E':
			b+=1
		if b==l:
			break
		d=max(d,b+1)
		while d<l and s[d]!='F':
			d+=1
		if d==l:
			break
		a+=1
		b+=1
		d+=1
		c+=1
print c

