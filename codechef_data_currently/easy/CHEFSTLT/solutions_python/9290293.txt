T = int(raw_input())

for i in range(T):
    s1 = raw_input()
    s2 = raw_input()
    compulsory = 0
    optional = 0
    for j in range(len(s1)):
        if (s1[j]=='?' or s2[j]=='?'):
            optional += 1
        elif s1[j] != s2[j]:
            compulsory += 1
        else:
            pass
    print '{} {}'.format(compulsory, compulsory+optional)
