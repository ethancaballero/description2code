t=input()
while(t>0):
	t-=1
	s=raw_input().strip()
	n=len(s);i=0;count=0
	while(i<n):
		if (s[i]!='4' and s[i]!='7'):
			count+=1
		i+=1
	print count