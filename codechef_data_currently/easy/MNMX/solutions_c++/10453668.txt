#include<iostream>
#include<algorithm>
using namespace std;
int main(){
int t;
long long int n,cost;
cin>>t;
while(t--){
    cin>>n;
    long long int a[n];
    for(int i=0;i<n;i++){
        cin>>a[i];
    }
    sort(a,a+n);
    cost=a[0]*(n-1);
    cout<<cost<<endl;
    }
    }
