T = int(raw_input())

for it in range(T):
    s = raw_input()
    max_bal = 0
    bal = 0
    for ch in s:
        if ch == '(':
            bal += 1
        else:
            bal -= 1
        max_bal = max_bal if max_bal > bal else bal
    st = ['(' for i in range(max_bal)] + [')' for i in range(max_bal)]
    print ''.join(st)
