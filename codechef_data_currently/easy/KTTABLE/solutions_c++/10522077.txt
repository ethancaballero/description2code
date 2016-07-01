#include<iostream>
using namespace std;
int main(){
int t,n;
cin>>t;
while(t--){
    cin>>n;
    long long int a[n+1],b;
    int c=0;
    a[0]=0;
    for(int i=1;i<=n;i++){
        cin>>a[i];
    }
    for(int i=0;i<n;i++){
        cin>>b;
        if(b<=(a[i+1]-a[i])) c++;
    }
    cout<<c<<endl;
}
}
