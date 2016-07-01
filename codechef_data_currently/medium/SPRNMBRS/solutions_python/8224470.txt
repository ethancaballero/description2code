t = input()
while t:
	L, R = map(int,raw_input().split())
	answer = 0

	value = 2
	while( value <= R ):
	    current = value
	    while current <= R:
	        if L <= current <= R:
	            answer+=1
	        current *= 3
	    value *= 2


	if L <= 1 <= R:
	    answer+=1

	print answer
	t-=1