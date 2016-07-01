#include<iostream>
using namespace std;
int main(){
int t,n,f,l;
cin>>t;
while(t--){
    cin>>n;
    f=n%10;
    for(int i=0;n>0;i++){
        l=n%10;
        n=n/10;
    }
    cout<<f+l<<endl;
}
}
