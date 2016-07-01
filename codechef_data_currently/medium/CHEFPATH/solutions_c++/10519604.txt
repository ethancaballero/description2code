using namespace std;

#include "bits/stdc++.h"

typedef long long LL;

int main() {
	int t;
	LL n,m;
	cin >> t;
	while(t--) {
		cin >> n >> m;
		if(n > m)	swap(n,m);
		if(n==1 && m==1) {
			puts("No");
			continue;
		}
		if(n == 1) {
			if(m == 2) {
				puts("Yes");
			} else {
				puts("No");
			}
		}	else {
			if(n&1 && m&1) {
				puts("No");
			} else {
				puts("Yes");
			}
		}
	}
	return 0;
}
