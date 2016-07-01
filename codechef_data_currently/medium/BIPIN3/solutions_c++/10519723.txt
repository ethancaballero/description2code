using namespace std;

#include "bits/stdc++.h"

typedef long long LL;

LL MOD=1e9+7;

LL modpow(LL a, LL b) {
	LL res = 1;
	while(b) {
		if(b&1) {
			res = (res * a) % MOD;
		}
		b >>= 1;
		a = (a * a) % MOD;
	}
	return res;
}

int main() {
	int t;
	LL n,k;
	cin >> t;
	LL ans;
	while(t--) {
		cin >> n >> k;
		ans = k;
		ans = (ans * modpow(k-1,n-1)) % MOD;
		cout << ans << endl;	
	}
	return 0;
}
