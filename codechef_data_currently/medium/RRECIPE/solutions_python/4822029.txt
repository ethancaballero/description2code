def main():
    for i in xrange(int(raw_input())):
        s = raw_input()
        ctr = 1
        for j in xrange((len(s)+1)//2):
            if s[j]=="?" and s[-j-1]=="?":
                ctr*=26
                ctr%=10000009
            elif s[j]!=s[-j-1] and s[j]!="?" and s[-j-1]!="?":
                ctr=0
                break
        print ctr
    return
 
main()