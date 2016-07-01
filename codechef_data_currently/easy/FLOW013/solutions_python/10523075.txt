for i in range(int(raw_input())):
    a, b, c = map(int, raw_input().split())
    if a + b + c == 180:
        if a == 180 or a == 0:
            print "NO"
        else:
            print "YES"
    else:
        print "NO"
