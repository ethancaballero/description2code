def solve(a):
	return "010" in a or "101" in a
for _ in xrange(input()):
	print "Good" if solve(raw_input()) else "Bad"