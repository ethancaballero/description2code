from math import*
for i in range(input()):
	a,b=map(float,raw_input().split())
	c=pow((b*b-a*a),0.5)
	d=pow((b*b+a*a),0.5)
	print ("%f %f")%(c,d)