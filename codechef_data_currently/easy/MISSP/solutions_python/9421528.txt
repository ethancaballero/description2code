T = int(raw_input())

for i in range(T):
    N = int(raw_input())
    dolls = {}
    for j in range(N):
        a = int(raw_input())
        if dolls.get(a,0):
            dolls[a] += 1
        else:
            dolls[a] = 1
    
    for key in dolls:
        if dolls[key] % 2:
            print key
            break
    
