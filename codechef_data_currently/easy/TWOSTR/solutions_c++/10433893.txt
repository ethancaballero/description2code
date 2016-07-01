#include<iostream>
#include<string>
using namespace std;
int main(){
int t,f=0;
string x,y;
cin>>t;
while(t--){
    cin>>x>>y;
    for(int i=0;i<x.length();i++){
        if(x[i]==y[i]||x[i]=='?'||y[i]=='?'){
            f=0;
        }
        else {f=1;break;}
    }
    if(f==1) cout<<"No"<<endl;
    else cout<<"Yes"<<endl;

}
}
