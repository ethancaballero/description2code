#include<bits/stdc++.h>
#define ll long long int
using namespace std;
int main()
{
	ll n,m,h,i,t,c,sum=0,tot=0,sub;
	vector<pair<ll,ll> > v;
	scanf("%lld%lld%lld",&n,&m,&h);
	for(i=0;i<h;i++)
	{
		scanf("%lld%lld",&t,&c);
		v.push_back(make_pair(c,t));
	}
	tot = n*m;
	sort(v.begin(),v.end());
	for(i=0;i<h;i++){
	
			sub = min(v[i].second,tot);
			sum+=sub*v[i].first;
			tot -= sub;
	
	}
	if(tot!=0)
		cout<<"Impossible";
	else
		cout<<sum;
		
return 0;
}