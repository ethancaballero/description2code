from __future__ import print_function


def set_diff(a_num, n, mod):
    a_num.sort()
    min_sum = 0
    max_sum = 0
    for ind in xrange(n):
        min_sum = (2 * min_sum + a_num[ind]) % mod
        max_sum = (2 * max_sum + a_num[n-1-ind]) % mod
    return (max_sum + mod - min_sum) % mod


def main():
    tc = int(raw_input())
    for _ in xrange(tc):
        a_len = int(raw_input())
        a_num = map(int, raw_input().split())
        print (set_diff(a_num, a_len, 10**9 + 7))


if __name__ == '__main__':
    main()
