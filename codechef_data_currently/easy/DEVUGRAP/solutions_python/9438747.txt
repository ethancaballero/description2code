T = int(raw_input())

for it in range(T):
    N, k = map(int, raw_input().split())
    x = map(int, raw_input().split())
    y = map(lambda a: a%k if ((a%k <= k/2) and (a - a%k != 0)) else (k - a%k), x)
    print sum(y)
