#include<iostream>
using namespace std;
int main(){
int t,n;
cin>>t;
while(t--){
    cin>>n;
    int a[n];
    int c1=0,c2=0;
    for(int i=0;i<n;i++){
        cin>>a[i];
    }
    for(int j=0;j<n;j++){
        for(int i=0;i<j;i++){
            if(a[i]>a[j]) c1++;
        }
    }
    for(int i=0;i<n-1;i++){
        if(a[i]>a[i+1]) c2++;
    }
    if(c1==c2) cout<<"YES"<<endl;
    else cout<<"NO"<<endl;
}
}
