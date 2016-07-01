_ = int(raw_input())
for __ in range(_):
    N = int(raw_input())
    arr = map(int,raw_input().split())
    ans = 0
    mx = 10**4 + 10
    for num in arr :
        if num < 2:
            ans = -1
            break
        ans = ans + num
        if num < mx:
            mx = num
    if ans != -1:
        ans = ans - mx + 2
    print ans