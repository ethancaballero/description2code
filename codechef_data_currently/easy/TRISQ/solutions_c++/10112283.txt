#include<bits/stdc++.h>
using namespace std;

typedef long long int ll;

void solve()
{
	ll N;
	cin>>N;
	N/=2;
	cout<<(N*(N-1))/2<<endl;
}

int main()
{
	int T;
	scanf("%d",&T);
	while(T--){
		solve();
	}
	return 0;
}
