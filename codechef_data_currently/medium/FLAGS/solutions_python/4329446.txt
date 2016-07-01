def calc_flags(n):
    sum = 0
    sum += 2*(n*(n-1) + n*(n-1)*(n-2))
    sum += n*(n-1)*(n-2)
    sum += 2*(n*(n-1)*(n-2) + n*(n-1)*(n-2)*(n-3))
    return sum
t = input()
while(t):
    n = input()
    print calc_flags(n)
    t = t-1
