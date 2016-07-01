#include<iostream>
using namespace std;
int main(){
int t;
long int a,b;
cin>>t;
for(int i=0;i<t;i++){
    cin>>a;
    cin>>b;
    if(a>b) cout<<a<<" ";
    else cout<<b<<" ";
    cout<<a+b<<endl;
}
}
