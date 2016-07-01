n = int(raw_input())
a = raw_input()
b = map(int,a.split())
s = sum(b)

if s%2:
    print max(n,s/2+1)

else:
    print max(n,s/2)