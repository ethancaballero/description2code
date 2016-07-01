#include<bits/stdc++.h>

using namespace std;

#define fin freopen("i1.txt","r",stdin)
#define pb(x) push_back(x)
#define mp(x,y) make_pair(x,y)
#define fastio ios_base::sync_with_stdio(false); cin.tie(0);
#define ll long long

const ll MAX=1000002;
ll n,q;
ll BIT[MAX+3];  // 1 based index

void update(ll x,ll v){
    for(ll i=x;i<=n;i+=i&-i)
        BIT[i]+=v;
}

ll getSum(ll idx){
    ll ans=0;
    for(ll i=idx;i>0;i-=i&-i)
        ans+=BIT[i];
    return ans;
}

int main(){
    //fin;
    cin>>n>>q;

    for(ll i=1;i<=n;i++) {
        ll p;
        cin>>p;
        for(ll k=i;k<=n;k+=k&-k)
            BIT[k]+=p;
    }
    while(q--) {
        char type;
        ll x,y;
        cin>>type>>x>>y;

        if(type=='S'){
            cout<<getSum(y+1)-getSum(x)<<endl;
        }
        else if(type=='G') {
            update(x+1,y);
        }
        else {
            update(x+1,-1*y);
        }
    }
    return 0;
}
