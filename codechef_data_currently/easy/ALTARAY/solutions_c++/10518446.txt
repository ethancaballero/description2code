#include<iostream>
using namespace std;
int main(){
std::ios::sync_with_stdio(false);
int t,n;
cin>>t;
while(t--){
    cin>>n;
    long long int a[n];
    int c[n+1];
    c[n-1]=1;

    for(int i=0;i<n;i++){
        cin>>a[i];
    }
    for(int i=n-2;i>=0;i--){
        if(a[i]*a[i+1]<0) c[i]=c[i+1]+1;
        else c[i]=1;
    }
    for(int i=0;i<n;i++){
        cout<<c[i]<<" ";
    }
    cout<<endl;
}
}
