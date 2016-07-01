#include<iostream>
using namespace std;
int main(){
int t,c,flag=0;
string feed;
cin>>t;
while(t--){
    cin>>feed;
    flag=0;
    c=(feed.length())-2;
    for(int i=0;i<c;i++){
        if(feed[i]=='0' && feed[i+1]=='1' && feed[i+2]=='0') {flag=1;break;}
        else if(feed[i]=='1' && feed[i+1]=='0' && feed[i+2]=='1') {flag=1;break;}
    }
    if(flag==1) cout<<"Good"<<endl;
    else cout<<"Bad"<<endl;
}
}
