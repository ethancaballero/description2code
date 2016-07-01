#include<bits/stdc++.h>
#define MOD 100000007
using namespace std;

long long int fast_exp(long long int b, long long int e)
{
    long long int r=1;
    while(e>0)
    {
       if(e&1) r=(r*b)%MOD;
       b=(b*b)%MOD;
       e/=2;
    }
    return r;
}

int main()
{
    ios_base::sync_with_stdio(0);
    int t;
    int inv2 = fast_exp(2,MOD-2);
    long long int n,a,b,c,r;
    cin>>t;
    while(t--)
    {
        cin>>n;

        r = fast_exp(3,n);
        a = (r + 1)%MOD;
        a = (a * inv2)%MOD;
        b = (a - fast_exp(2,n) + MOD)%MOD;

        c = (fast_exp(4,n-1)*2)%MOD;
        c += fast_exp(2,n);
        c = c%MOD;
        c += fast_exp(2,n-1);
        c = c%MOD;
        c = (MOD+c-r)%MOD;
        c = (MOD+c-a)%MOD;

        cout<<b<<" "<<c<<endl;

    }
    return 0;
}
