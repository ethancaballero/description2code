import math,sys
from math import pow
from sys import stdin 
def main():
	t = sys.stdin.readline()
	t = int(t)
	temp = 0.0000000
	while(t):
		x,k = map(int, sys.stdin.readline().split(' '))
		i=1
		while(1):
			if pow(2,i)>k:
				temp = i
				break
			else:
				i = i+1
		sum  = (x/pow(2,temp))+ ((k-pow(2,temp-1))*x/pow(2,temp-1))
		print format(sum,'.17f')
		t = t-1
if __name__=="__main__":
	main()