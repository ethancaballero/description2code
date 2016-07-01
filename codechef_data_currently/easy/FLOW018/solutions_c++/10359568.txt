#include<iostream>
using namespace std;
int main(){
int t,n;
long long int fact;
cin>>t;
while(t--){
    cin>>n;
    fact=1;
    for(int i=1;i<=n;i++){
        fact*=i;
    }
    cout<<fact<<endl;
}
}
