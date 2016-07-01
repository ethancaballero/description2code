#cook your code here
t = int(raw_input())
for i in range(0,t):
    n,k = raw_input().split()
    n = int(n)
    k = int(k)
    res = ( k**n + k * ((-1)**n) ) / ( k + 1 )
    res %= 1000000007
    print res