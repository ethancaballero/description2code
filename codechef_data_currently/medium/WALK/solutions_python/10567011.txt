for _ in range(input()):
    n= int(raw_input())
    att = map(int,raw_input().split())
    ans = []
    for i in range(n):
        ans.append(att[i]+i)
    print max(ans)