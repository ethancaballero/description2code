#include<iostream>
using namespace std;
int main(){
int t,n,sum,d[8],c=0;
cin>>t;
for(int i=0;i<t;i++){
    sum=0;
    c=0;
    cin>>n;
    for(int j=0;n!=0;j++){
        d[j]=n%10;
        n=n/10;
        c+=1;
    }
    for(int k=0;k<c;k++){
        sum+=d[k];
    }
    cout<<sum<<endl;
}
}
