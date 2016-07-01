T = int(raw_input())

for i in range(T):
    N = int(raw_input())
    p = []
    for j in range(N):
        p.append(map(int, raw_input().split()))
    res = 0
    for j in range(1, N+1):
        res = res ^ j
    print res
