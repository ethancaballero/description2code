import math

# b1 = n+2 . b2 = 3*n

def lamb(n , b1 , b2 , q):
	
	temp = 0
#	print b1,b2

	if((q<b1) or (q>b2)):
		#print "In here"
		return 0
	else:
		temp = q - n - 1
		if(temp > n):
			temp = 2*n - temp
	return temp

def main():
	x = raw_input()
	x = x.split()
	x = map(int , x)

	n = x[0]
	m = x[1]

	for i in range(0,m):
		q = raw_input()
		q = int(q)

		ans = lamb(n,n+2,3*n,q)

		print ans



if __name__ == '__main__':
	main()