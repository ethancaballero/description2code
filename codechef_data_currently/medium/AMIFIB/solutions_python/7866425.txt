
def main():
	a=0
	b=1
	c=1
	count={0:1,1:1}
	while c<10**1001:
		a,b=b,c
		c=a+b
		count[c]=1

	tc=input()
	import sys
	inp=map(int,sys.stdin.read().split())

	for i in inp:
		try:
			count[i]
			print("YES")
		except:
			print("NO")

if __name__=="__main__":
	main()
