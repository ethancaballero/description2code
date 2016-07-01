using namespace std;

#include "bits/stdc++.h"

typedef long long LL;

LL MOD = 1e9+7;

LL A[1005];

LL dp1[1005];
LL dp2[1005];

int main() {
	int t;
	cin >> t;
	int n,m,s;
	while(t--) {
		cin >> n >> m >> s;
		s--;
		for(int i = 0 ; i < m ; ++i)	{
			cin >> A[i];	
		}
		for(int i = 0 ; i < n ; ++i)	{
			dp1[i] = 0;
		}	
		dp1[s] = 1;
		for(int i = 0 ; i < m ; ++i) {
			for(int j = 0 ; j < n ; ++j) {
				if(j-A[i] >= 0)	{
					dp2[j] = (dp2[j] + dp1[j-A[i]]) % MOD;
				}
				if(j+A[i] < n) {
					dp2[j] = (dp2[j] + dp1[j+A[i]]) % MOD;
				}
			}
			for(int j = 0 ; j < n ; ++j) {
				dp1[j] = dp2[j];
				dp2[j] = 0;
			}
		}
		for(int i = 0 ; i < n ; ++i)	{
			cout << dp1[i] << " ";
		}
		cout << endl;
	} 
	return 0;
}
