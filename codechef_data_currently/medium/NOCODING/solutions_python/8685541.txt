tc = input()
alpha = { 'a' :0 ,'b' :1 ,'c' :2 ,'d' :3 ,'e' :4 ,'f' :5 ,'g' :6 ,'h' :7 ,'i' :8 ,'j' :9 ,'k' :10 ,'l' :11 ,'m' :12 ,'n' :13 ,'o' :14 ,'p' :15 ,'q' :16 ,'r' :17 ,'s' :18 ,'t' :19 ,'u' :20 ,'v' :21 ,'w' :22 ,'x' :23 ,'y' :24 ,'z' :25 }
for _ in xrange(tc):
	ins = 0
	w = raw_input()
	s = len(w)
	p1 = p2 = alpha[w[0]]
	for a in w:
		ins += 1
		p1 = alpha[a]
		if(p2<=p1):
			ins += p1-p2
		else:
			ins += 26-p2+p1
		p2 = p1
	ins += 1
	if(ins<=11*s):
		print "YES"
	else:
		print "NO"