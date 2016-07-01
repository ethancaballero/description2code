for x in xrange(input()):
	size, a, b = map(int,raw_input().split())
	print 2**size-2**abs(bin(a)[2:].count('1')+bin(b)[2:].count('1')-size)
