# Sum of palindromic numbers
# Problem code: SPALNUM
# https://www.codechef.com/problems/SPALNUM/



n=int(raw_input())
for i in range(0,n):
    a,b=map(int,raw_input().split())
    c=int(0)
    for j in range(a,b+1):
        x=j
        s=0
        y=str(j)
        l=len(y)
        if l%2==0:
            if y[:l/2]==y[l/2:l]:
                c=c+j
        else:
            if y[:l/2]==y[(l+1)/2:l]:
                c=c+j
    print c