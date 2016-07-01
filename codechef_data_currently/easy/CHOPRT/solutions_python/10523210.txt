for i in range(int(raw_input())):
    a, b = map(int, raw_input().split())

    if a == b:
        print "="
    elif a > b:
        print ">"
    else:
        print "<"
