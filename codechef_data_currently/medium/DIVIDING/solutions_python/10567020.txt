n=input()
arr=map(int,raw_input().split())
if(n*(n+1)/2==sum(arr)):
	print "YES"
else:
	print "NO"