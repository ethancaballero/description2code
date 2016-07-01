def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
 
t = input()
for _ in xrange(t):
    arr = map(int, raw_input().split())
    arr.pop(0)
    g = reduce(gcd, arr)
    for i in arr:
        print i / g,
    print "" 

