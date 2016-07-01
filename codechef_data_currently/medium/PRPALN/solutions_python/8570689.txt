number = int(raw_input())
 
for z in range (number):
    inp = raw_input()
    length = len(inp)
    count=0
 
    for i in range(length):
        fresh = inp [ :i] + inp [i+1: ]
        lenn = len(fresh)
        for q in range(0,lenn/2):
            if fresh[q] != fresh[lenn-q-1]:
                count= count+1
                break
    if length==count:
        print "NO"
    else:
        print "YES"
