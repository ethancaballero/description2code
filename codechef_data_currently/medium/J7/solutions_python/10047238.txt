t = input()
while(t>0):
	p,s =map(int, list(raw_input().split()))
	a = (p-pow(p*p-24*s,0.5))/12
	b = (p+pow(p*p-24*s,0.5))/12
	h = (p-8*a)/4
	h1 = (p-8*b)/4
	v= a*a*h
	v1 = b*b*h1
	if( v>v1 ):
		print("%.2f" % v)
	else:
		print("%.2f" % v1)
	t-=1