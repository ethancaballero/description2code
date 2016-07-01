#include<iostream>
using namespace std;
int main(){
int n;
long int c,sum=0,x;
cin>>n;
for(int i=0;i<n;i++){
    cin>>c;
    sum+=c;
}
x=(n*(n+1))/2;
if(sum==x) cout<<"YES"<<endl;
else cout<<"NO"<<endl;
}
