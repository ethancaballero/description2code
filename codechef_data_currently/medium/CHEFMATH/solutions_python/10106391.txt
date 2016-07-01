ans=0
found=set()
def numberofways(fib,x,k,curr,idx,high):
	global ans
	if ( x!=0 and curr>=k ) or x<0 or x>(high*(k-curr)):
		# print 'Discarded'
		return 0
	if x==0 and curr==k:
		ans+=1
		# print 'New Way'
		return 1	
	for i in xrange(0,49):
		if fib[i]>x or fib[i]>high:
			break
		else:
			# print 'fib', fib[i], 'i', curr+1
			numberofways(fib,x-fib[i],k,curr+1,i, fib[i])
	return ans
 
 
q=int(input())
fib=[1,2]
for i in xrange(2,50):
	fib.append(fib[i-1]+fib[i-2])
while q>0:
	s1=raw_input().split()
	x,k=[int(i) for i in s1]
	ans=0
	numberofways(fib, x, k, 0,0,x+1)
	print ans%1000000007
	q-=1 