#include<iostream>
using namespace std;
int main(){
int t;
long int n,x;
cin>>t;
while(t--){
    cin>>n;
    if((n%4)==1) cout<<"ALICE"<<endl;
    else cout<<"BOB"<<endl;
}
}
