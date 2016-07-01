import bisect
import time
import sys
A = []
subarray = {}
keys = []
subarray_low = {}
subarray_high = {}
subarray_length = 0
# (val,start,pos) stack
# (start,end,pos) dict

def preprocess(n):
	global keys
	global A
	global subarray
	global subarray_low
	global subarray_high
	global subarray_length

	for i in A:
		subarray[i] = 0
	stack = []
	for i in range(n):
		if i == 0:
			stack.append((A[0],0,0))
		else:
			top = stack[-1]
			if A[i] <= top[0]:
				stack.append((A[i],i,i))
			else:
				while len(stack) > 0 and A[i] > stack[-1][0]:
					top = stack[-1]
					stack.pop()
					subarray[top[0]] += (i-top[2]) * (top[2]-top[1]+1)
				stack.append((A[i],top[1],i))
	end = n-1

	length = len(stack)
	i = 0
	while i<length:
		top = stack[-1]
		stack.pop()
		subarray[top[0]] += (end-top[2]+1)*(top[2]-top[1]+1)
		i += 1

	keys = sorted(subarray.keys())

	t = 0
	for i in keys:
		t += subarray[i]
		subarray_low[i] = t

	t = 0
	for i in reversed(keys):
		t += subarray[i]
		subarray_high[i] = t

	subarray_length = len(subarray)


def play(symbol,number,starter):
	global keys
	global A
	global subarray
	global subarray_low
	global subarray_high
	global subarray_length

	ans = 0
	if symbol == '<':
		k = bisect.bisect_left(keys,number)
		if k:
			ans = subarray_low[keys[k-1]]
	elif symbol == '=':
		if number in subarray:
			ans = subarray[number]
	else:
		k = bisect.bisect_right(keys,number)
		if k<subarray_length:
			ans = subarray_high[keys[k]]

	if ans%2 == 0:
		if starter == 'C':
			return 'D'
		else:
			return 'C'
	else:
		return starter



if __name__ == '__main__':
	n, m = map(int,sys.stdin.readline().split())
	A = map(int,sys.stdin.readline().split())
	preprocess(n)
	s = ''
	for j in range(m):
		C, K, X = sys.stdin.readline().split()
		K = int(K)
		s = s+play(C,K,X)
	print(s)

