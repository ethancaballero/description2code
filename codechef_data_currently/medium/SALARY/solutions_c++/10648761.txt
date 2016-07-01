#include<iostream>
using namespace std;
int main(){
ios::sync_with_stdio(false);
int t,n,w;
cin>>t;
while(t--){
    cin>>n;
    int sum=0,minw=10000;
    for(int i=0;i<n;i++){
        cin>>w;
        sum+=w;
        if(w<minw) minw=w;
    }
    cout<<sum-(n*minw)<<endl;
}
}
