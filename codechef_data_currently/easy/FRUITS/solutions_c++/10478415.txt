#include<iostream>
using namespace std;
int main(){
int t,n,m,k,ans;
cin>>t;
while(t--){
    cin>>n>>m>>k;
    for(int i=0;i<k;i++){
        if(m>n) n+=1;
        else if (n>m)m+=1;
        else break;
    }
    if(m>n) ans=m-n;
    else ans=n-m;
    cout<<ans<<endl;
}
}
