def gcd(a,b):
    while(b):
        a,b=b,a%b
    return a
t=input()
while(t):
    a,b=map(int,raw_input().split())
    print(gcd(a,b))
    t=t-1;