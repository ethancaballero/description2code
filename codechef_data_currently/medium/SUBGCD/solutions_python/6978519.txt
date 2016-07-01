import math
from fractions import gcd

def main():
	t= raw_input()
	t = int(t)
	for i in range(0,t):
		n = raw_input()
		n= int(n)
		arr = raw_input()
		arr = arr.split()
		arr = map(int,arr)
		temp = 1
		start = arr[0]
		flag = False
		for k in range(1,n):
			temp = gcd(start,arr[k])
			if( temp == 1):
				print n
				flag = True
				break
			else:
				start = temp
		if flag == False:
			print "-1"


if __name__ == '__main__':
	main()