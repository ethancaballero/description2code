# Got this better solution with the help of sharad07

for t in range(input()):
    h, m = map(int , raw_input().split())
    count = 0 
    a = min(h, 10) # single digit hours
    b = min(m, 10) # single digit minutes 
    # no. of hours between 0..h-1 and 0..m-1 and mulitple of 11
    c = (h-1)/11 
    d = (m-1)/11 
    count  = min(a, b) + min(a-1,d) + min(c, b-1) + min(c,d)
    print count
