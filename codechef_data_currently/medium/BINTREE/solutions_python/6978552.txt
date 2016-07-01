import math

def findlevel(n):
	
	first = 1
	second = 2
	level = 1

	while(1):
		if(n >= first and n < second):
			return level
		else:
			first = first*2
			second = second*2
			level = level+1

def process(m,n):
	level1 = findlevel(m)
	level2 = findlevel(n)

	difflev = abs(level2 - level1)

	steps = difflev
	#print difflev

	if(level2 > level1):
		n /= int(math.pow(2,difflev))
	if(level1 > level2):
		m /= int(math.pow(2,difflev))

	#print m,n

	while(m != n):
		steps = steps+2
		m = int(m/2)
		n = int(n/2)
		#print m,n
	return steps

def main():
	t = raw_input()
	t = int(t)
	for i in range(0,t):
		
		x = raw_input()
		x = x.split()
		x = map(int,x)
		ans = process(x[0],x[1])
		print ans


if __name__ == '__main__':
	main()