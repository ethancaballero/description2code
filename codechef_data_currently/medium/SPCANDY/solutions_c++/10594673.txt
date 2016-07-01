#include<iostream>
using namespace std;
int main(){
int t;
long long int n,k;
cin>>t;
while(t--){
    cin>>n>>k;
    if(k==0) cout<<"0"<<" "<<n<<endl;
    else cout<<n/k<<" "<<n%k<<endl;
}
}
