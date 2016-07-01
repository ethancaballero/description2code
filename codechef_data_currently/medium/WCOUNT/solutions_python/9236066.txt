import math

for _ in range(input()):
    s = raw_input()
    l = len(s)
    counted = {}
    for j in range(0,l,1):
        if s[j] not in counted:
            counted[s[j]] = 1
        else:
            counted[s[j]]+=1
    m = math.factorial(len(s))
    for i in counted.itervalues():
        if i>1:
            f = math.factorial(i)
            m /= f
    print m % (1000000007)
