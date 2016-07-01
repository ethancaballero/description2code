#include<iostream>
using namespace std;
int main(){
ios::sync_with_stdio(false);
int t;
long long int n,a;
cin>>t;
while(t--){
    cin>>n;
    for(int i=0;i<n;i++){
        cin>>a;
    }
    cout<<(n*(n-1)/2)<<endl;
}
}
