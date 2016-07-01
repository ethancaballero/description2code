def binary_search(l, value):
    low = 0
    high = len(l)-1
    while low <= high: 
        mid = (low+high)//2
        if l[mid] > value: high = mid-1
        elif l[mid] < value: low = mid+1
        else: return mid
    return -1

# 4782th fibonacci no. has 1000 digits
T = int(raw_input())

a = 1 
b = 1
fib = [a, b]
for x in range(2, 4787):
	fib.append(fib[x - 1] + fib[x - 2])


i = 0
while i < T:
	A = int(raw_input())
	if binary_search(fib, A) >= 0:
		print 'YES'
	else:
		print 'NO'
	i = i + 1