#include<iostream>
#include<algorithm>
using namespace std;
int main(){
int t,n;
long int a[100000];
cin>>t;
for(int i=0;i<t;i++){
    cin>>n;
    for(int j=0;j<n;j++){
        cin>>a[j];
    }
    sort(a,a+n);
    cout<<a[0]+a[1]<<endl;

}
}
