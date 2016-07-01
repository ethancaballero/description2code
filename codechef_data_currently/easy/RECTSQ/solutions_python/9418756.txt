T = int(raw_input())

for i in range(T):
    l, b = map(int, raw_input().split())
    x, y = l, b
    while y:
        temp = y
        y = x % y
        x = temp
    gcd = x
    print (l/gcd) * (b/gcd)
    
