s = raw_input()
c, h, e, f = 0, 0, 0, 0
for ch in s:
    if ch == 'C':
        c += 1
    elif ch == 'H':
        if h < c:
            h += 1
    elif ch == 'E':
        if e < h:
            e += 1
    elif ch == 'F':
        if f < e:
            f += 1
print f
