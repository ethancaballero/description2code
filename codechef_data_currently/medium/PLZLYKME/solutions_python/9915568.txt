def solve(l, d, s, c):
	if d > 31: return 'ALIVE AND KICKING'
	return 'ALIVE AND KICKING' if s*(c+1)**(d-1) >= l else 'DEAD AND ROTTING'
for _ in xrange(input()):
	print(solve(*map(int, raw_input().split())))
