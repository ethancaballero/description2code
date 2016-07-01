T = int(raw_input())

for it in range(T):
    n = int(raw_input())
    A = map(int, raw_input().split())
    count = 0
    for i in range(n):
        _sum = 0
        product = 1
        j = i
        while (j<n):
            _sum += A[j]
            product *= A[j]
            if _sum == product:
                count += 1
            j += 1
    print count
