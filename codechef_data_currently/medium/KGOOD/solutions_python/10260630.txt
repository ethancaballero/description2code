test = int(raw_input())
for _ in range(test):
    inp = raw_input().split()
    word = inp[0]
    k = int(inp[1])

    freq = {}
    for c in word:
        if c not in freq:
            freq[c] = 1
        else:
            freq[c] += 1
    ret = float('inf')
    for d in freq:
        curr_ret = 0
        for c in freq:
            if freq[c] - freq[d] > k:
                curr_ret += (freq[c] - freq[d] - k)
            if freq[c] < freq[d]:
                curr_ret += freq[c]
        ret = min(ret, curr_ret)
    print ret