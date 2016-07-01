#include<iostream>
using namespace std;
int main(){
int t,n,k;
cin>>t;
while(t--){
    cin>>n>>k;
    int m=0;
    while(k>0){
        if(n%k>m){
            m=n%k;
        }
        k--;
    }
    cout<<m<<endl;
}
}
