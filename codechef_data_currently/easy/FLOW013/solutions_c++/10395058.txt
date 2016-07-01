#include<iostream>
using namespace std;
int main(){
int t,a,b,c;
cin>>t;
while(t--){
    cin>>a>>b>>c;
    if(a+b+c==180 && a>0 && b>0 && c>0) {
        cout<<"YES"<<endl;
    }
    else cout<<"NO"<<endl;
}
}
