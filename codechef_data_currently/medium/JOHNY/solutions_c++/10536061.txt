#include<iostream>
#include<algorithm>
using namespace std;
int main(){
int t,n,len,k;
cin>>t;
while(t--){
    cin>>n;
    long int a[n];
    for(int i=0;i<n;i++){
        cin>>a[i];
    }
    cin>>k;
    len=a[k-1];
    sort(a,a+n);
    for(int i=0;i<n;i++){
        if(a[i]==len){
            cout<<i+1<<endl;
            break;
        }
    }
}
}
