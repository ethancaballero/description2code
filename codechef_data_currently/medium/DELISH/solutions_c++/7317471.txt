/*
Using dynamic programming, we find maxLeft[i] is the maximal value of the sum of consecutive numbers that are in the left of i (including i).
minLeft, maxRight, minRight are defined in the similar way.

the result is max(abs(maxRight[i+1] - minLeft[i]), abs(minRight[i+1] - minLeft[i]), abs(minRight[i+1] - maxLeft[i]), abs(minRight[i+1] - minLeft[i])) for all i;
*/

#pragma comment(linker, "/STACK:16777216")
#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <string>
#include <memory.h>
#include <sstream>
#include <complex>

#define FOR(i,a,b) for (int i = (a), _b = (b); i <= _b; i++)
#define FORD(i,a,b) for (int i = (a), _b = (b); i >= _b; i--)

using namespace std;

int a[12222], n;
long long minLeft[12222], maxLeft[12222], minRight[12222], maxRight[12222];

int main() {
    int ntest;
    cin >> ntest;

    while (ntest--) {
        scanf("%d", &n);
        FOR (i, 1, n)
            scanf("%d", a + i);

        minLeft[1] = maxLeft[1] = a[1];
        FOR (i, 2, n) {
            minLeft[i] = min(minLeft[i - 1] + a[i], (long long) a[i]);
            maxLeft[i] = max(maxLeft[i - 1] + a[i], (long long) a[i]);
        }

        minRight[n] = maxRight[n] = a[n];
        FORD (i, n - 1, 1) {
            minRight[i] = min(minRight[i + 1] + a[i], (long long) a[i]);
            maxRight[i] = max(maxRight[i + 1] + a[i], (long long)  a[i]);
        }

        long long res = 0;

        FOR (i, 1, n - 1) {
            res = max(res, abs(minLeft[i] - maxRight[i+ 1]));
            res = max(res, abs(minLeft[i] - minRight[i+ 1]));
            res = max(res, abs(maxLeft[i] - maxRight[i+ 1]));
            res = max(res, abs(maxLeft[i] - minRight[i+ 1]));
        }

        cout << res << endl;
    }
    return 0;
}
