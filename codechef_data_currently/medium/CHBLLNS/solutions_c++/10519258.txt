using namespace std;

#include "bits/stdc++.h"

typedef long long LL;

int main() {
	int t;
	cin >> t;
	LL r,g,b,k;
	while(t--) {
		cin >> r >> g >> b >> k;
		cout << min(k-1,r) + min(k-1,g) + min(k-1,b) + 1 << endl;
	}
	return 0;
}
