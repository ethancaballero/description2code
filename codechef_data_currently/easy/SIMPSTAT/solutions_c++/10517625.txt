#include<iostream>
#include<algorithm>
#include<iomanip>
using namespace std;
int main(){
int t,n,k;
cin>>t;
while(t--){
    cin>>n>>k;
    int a[n],div;
    long double sum=0;
    double avg;
    for(int i=0;i<n;i++)
        cin>>a[i];
    sort(a,a+n);
    for(int i=k;i<n-k;i++){
        sum+=a[i];
    }
    div=n-(2*k);
    avg=sum/div;
    cout<<fixed<<setprecision(6)<<avg<<endl;
}
}
