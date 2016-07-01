import sys

def compute(a,b,c):
	x=a+b
	y=''
	for i in range(0,c.__len__()):
		y=y+c[i]
	statx=[0]*150
	staty=[0]*150
	for i in range(0,x.__len__()):
		temp=ord(x[i])
		statx[temp]=statx[temp]+1
	for i in range(0,y.__len__()):
		temp=ord(y[i])
		staty[temp]=staty[temp]+1

	for i in range(0,150):
		if(staty[i]>statx[i]):
			return 0


	return 1


def main():
	tc=input()
	while(tc):
		a,b=raw_input().split()
		n=input()
		c=[]
		for i in range(0,n):
			temp=raw_input()
			c.append(temp)
		flag=compute(a,b,c)
		if flag==1:
			print "YES"
		else:
			print "NO"


		tc=tc-1

main()
sys.exit(0)