"""
 Problem: Chef team
 URL: http://www.codechef.com/problems/CHEFTEAM
"""

__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"


t = int(raw_input())
for i in range(t):
    line = raw_input()
    (n, k) = line.split()
    n = int(n)
    k = int(k)
    if k > n:
        print 0
    else:
        if (k < (n - k)):
            k = n - k

        numerator = 1
        for i in range(k + 1, n + 1):
            numerator = numerator * i  

        denominator = 1
        for j in range(1, n - k + 1):
            denominator = denominator * j
        print numerator/denominator
