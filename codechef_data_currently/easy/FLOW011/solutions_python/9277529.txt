T = int(raw_input())

for i in range(T):
    b = int(raw_input())
    if b<1500:
        hra = 0.10 * b
        da = 0.90 * b
    else:
        hra = 500
        da = 0.98* b
    print '%g' % (b+hra+da)
    
