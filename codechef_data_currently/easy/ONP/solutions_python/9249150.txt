for i in range(int(raw_input())):
    stack = []
    res = []
    for ch in raw_input():
        if ch == '(':
            pass
        elif ch == ')':
            res.append(stack.pop())
        elif ch in "+-/*^%":
            stack.append(ch)
        else:
            res.append(ch)
    print ''.join(res)
