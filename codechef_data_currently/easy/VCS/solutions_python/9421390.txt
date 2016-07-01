T = int(raw_input())

for i in range(T):
    N, M, K = map(int, raw_input().split())
    
    # Create blank array of N elements of all 0 values
    seq = [0 for j in range(N)]
    
    A = map(int, raw_input().split())
    B = map(int, raw_input().split())
    
    # Or the corresponding element with 1
    for j in A:
        seq[j-1] = seq[j-1] | 1
    
    # Or the corresponsding element with 2
    for j in B:
        seq[j-1] = seq[j-1] | 2
    
    # Now, Pick only elements with value 0 or 3
    total_tracked_ignored = 0
    total_untracked_unignored = 0
    for element in seq:
        if element == 0:
            total_untracked_unignored += 1
        elif element == 3:
            total_tracked_ignored += 1
    
    print "{} {}".format(total_tracked_ignored, 
                          total_untracked_unignored)
