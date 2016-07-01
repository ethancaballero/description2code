T = int(raw_input())

for it in range(T):
    N = int(raw_input())
    N2 = []
    for i in range(N):
        N2.append(map(int, raw_input().split()))
    
    mapping = [[0,0] for i in range(1, N**2 + 1)]
    for i in range(N):
        for j in range(N):
            mapping[N2[i][j] - 1] = [i, j]
    
    steps = 0
    curr = mapping[0]
    for i in range(1, N**2):
        dest = mapping[i]
        steps +=  abs(curr[0]-dest[0])
        curr[0] = dest[0]
        steps +=  abs(curr[1]-dest[1])
        curr[1] = dest[1]
    print steps
