#include<iostream>
using namespace std;
int main(){
int t;
string a,b;
cin>>t;
while(t--){
    cin>>a>>b;
    int f=0;
    for(int i=0;i<a.length();i++){
        for(int j=0;j<b.length();j++){
            if(a[i]==b[j])
                {f=1;break;}
        }
        if(f==1) break;
    }
    if(f==1) cout<<"Yes"<<endl;
    else cout<<"No"<<endl;
}
}
