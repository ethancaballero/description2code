jc, sc, m = map(int, raw_input().split())
m -= jc 
temp = m/sc 
if temp%2 == 0 :
    print "Lucky Chef"
else:
    print "Unlucky Chef"
