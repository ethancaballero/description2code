t= input()
count=0
while(t>0):
	t-=1
	a1,a2,b1,b2,c1,c2=map(int,raw_input().split())
	A=(a1-b1)**2 +(a2-b2)**2
	B=(b1-c1)**2+(b2-c2)**2
	C=(a1-c1)**2+(a2-c2)**2
	if( A+B==C or B+C==A or C+A==B ):
		count+=1
print count