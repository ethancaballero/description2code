#include<cmath>
#include<iostream>
 
using namespace std;
 
#define e 1e-9
#define MOD 1000000007
 
long long v[35000];
double f[35000];
 
int n;
long long res = 1;
 
void go(int i) {
    res = (res * v[i]) % MOD;
    if (i * 2 > n) return;
    if ((i * 2 + 1 > n) || (abs(f[i] - f[i * 2 + 1] - log(v[i])) > e)) go(i * 2);
    else go(i * 2 + 1);
}
 
int main() {
    int h;
 
    do {
 
        cin >> h;
        if (!h) break;
 
        n = (1 << h) - 1;
 
        for (int i = 1; i <= n; i++) cin >> v[i];
 
        for (int i = n; i >= 1; i--) {
            if (i * 2 > n) f[i] = log(v[i]);
            else {
                f[i] = f[i * 2];
                if (i * 2 + 1 <= n && f[i] < f[i * 2 + 1] - e)
                    f[i] = f[i * 2 + 1];
                f[i] += log(v[i]);
            }
        }
 
        res = 1;
 
        go(1);
 
        cout << res << endl;
 
    } while (1);
 
    return 0;
}
 