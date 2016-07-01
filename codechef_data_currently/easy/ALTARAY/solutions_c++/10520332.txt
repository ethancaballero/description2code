using namespace std;

#include "bits/stdc++.h"

int A[100005];

int dp[100005];

typedef long long LL;

int main() {
	int t;
	cin >> t;
	int n;
	LL num;
	while(t--) {
		cin >> n;
		for(int i = 0 ; i < n ; ++i) cin >> A[i], dp[i] = 1;
		for(int i = n - 2 ; i >= 0 ; i--) {
			num = (LL)(A[i]) * (LL)(A[i+1]);
			if(num < 0)	dp[i] = 1 + dp[i+1];		
		}
		for(int i = 0 ; i < n ; ++i)	cout << dp[i] << " ";
		cout << endl;
	}
	return 0;
}
