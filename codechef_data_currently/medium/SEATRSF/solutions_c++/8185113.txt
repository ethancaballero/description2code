#include<bits/stdc++.h>
using namespace std;
#define ll long long int
#define mod 1000000007

ll fmexp(ll base,ll expo)
{
    ll r=1;
    while(expo)
    {
        if(expo&1)r=(((r%mod)*(base%mod))%mod);
        base=((base%mod)*(base%mod))%mod;
        expo>>=1;
    }
    r=r%mod;
    return r;
}

int main()
{
    ios_base::sync_with_stdio(0);
    int t,k;
    ll n,m,q,r;
    cin>>t;
    while(t--)
    {
        cin>>n>>m>>q>>k;
        if(m<=q){r=0;goto a;}
        r=(((fmexp(q+1,n)+fmexp(q-1,n))%mod)-((2*fmexp(q,n))%mod)+mod)%mod;
        r*=(m-q);
        r=r%mod;
        a:
        cout<<r<<endl;
    }
    return 0;
}