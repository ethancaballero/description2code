#include<iostream>
using namespace std;
int main(){
int t,n,orig,rev;
cin>>t;
while(t--){
    cin>>n;
    orig=n;
    rev=0;
    for(int i=0;n>0;i++){
        rev*=10;
        rev+=n%10;
        n/=10;
    }
if(orig==rev) cout<<"wins"<<endl;
else cout<<"losses"<<endl;
}
}
