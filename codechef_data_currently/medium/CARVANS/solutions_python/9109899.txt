# cook your code here
for testcases in xrange(int(raw_input() ) ) :
    n = int(raw_input())
    Arr = map(int, raw_input().split() )
    m = Arr[0]
    c = 1
    for i in xrange(1, len(Arr)):
        if (Arr[i] <= m ):
            c += 1
            m = Arr[i]
    print c