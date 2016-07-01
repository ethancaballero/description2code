t = input()
for i in range(0,t):
    n = input()
    a = 9999999
    b = 9999999
    val = raw_input()
    val = val.split(" ")
    i=1
    for v in val:
        if i>n:
            break
        if int(v) < a:
            b = a
            a = int(v)
        elif int(v) < b:
            b = int(v)
        i = i+1
    print str(a+b)