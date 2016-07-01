def get_count(s, exp_str, n):
    b_lst = []
    g_lst = []
    for i in xrange(len(s)):
        if s[i] != exp_str[i]:
            if s[i] == 'B':
                b_lst.append(i)
            else:
                g_lst.append(i)
    result = 0
    for i in xrange(len(b_lst)):
        result += pow(abs(b_lst[i]-g_lst[i]), n)
    return result

def count_swaps(s, n):
    if len(s) == 1:
        return 0
    b_cnt = s.count('B')
    g_cnt = s.count('G')
    diff = abs(b_cnt - g_cnt)
    if diff > 1:
        return -1
    if n == 2:
        n = 1
    if b_cnt == g_cnt:
        exp_str = 'BG' * b_cnt
        result = get_count(s, exp_str, n)  
        exp_str = 'GB' * b_cnt
        return min(result, get_count(s, exp_str, n))
    elif b_cnt > g_cnt:
        exp_str = 'BG' * (g_cnt) + 'B'
    else:
        exp_str = 'GB' * (b_cnt) + 'G'
    return get_count(s, exp_str, n)

def solve():
   t = int(raw_input())
   for i in xrange(t):
       n = int(raw_input())
       s = raw_input()
       print count_swaps(s, n)

if __name__ == '__main__':
    solve()
