T = int(raw_input())

for it in range(T):
    len_a = int(raw_input())
    a = map(int, raw_input().split())
    
    len_f = int(raw_input())
    f = map(int, raw_input().split())
    
    isSub = True
    i, j = 0, 0
    while (j < len_f):
        if f[j] not in a:
            isSub = False
            break
        j += 1
        
    print "Yes" if (isSub) else "No"
