t = input()
while(t>0):
	t-=1
	arr=map(int,list(raw_input().split()[0]))
	print sum(arr)