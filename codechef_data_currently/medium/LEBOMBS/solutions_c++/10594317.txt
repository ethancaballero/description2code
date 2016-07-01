#include<iostream>
using namespace std;
int main(){
int t,n,prev;
string s;
cin>>t;
while(t--){
    int c=0,destroy=0;
    cin>>n;
    cin>>s;
    for(int i=0;i<n;i++){
        destroy=0;
        if(s[i]=='1') destroy=1;
        if(i>0 && s[i-1]=='1') destroy=1;
        if(i<n-1 && s[i+1]=='1') destroy=1;
        if(destroy==0) c++;
    }
    cout<<c<<endl;
}
}
