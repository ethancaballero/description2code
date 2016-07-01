n1,n2,n3 = map(int,raw_input().split())
arr = {}
for a in xrange(n1+n2+n3):
	tmp = input()
	try:
		arr[tmp] += 1
	except:
		arr[tmp] = 1
farr = []
for a in arr:
	if(arr[a]!=1):
		farr.append(a)
farr.sort()
print len(farr)
for a in farr:
	print a