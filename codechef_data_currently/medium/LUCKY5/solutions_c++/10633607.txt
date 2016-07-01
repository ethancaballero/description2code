//Same Logic, increased I/O Speeds
#include<iostream>
using namespace std;
int main(){
ios::sync_with_stdio(false);
int t,c4,c7,diff;
string n;
cin>>t;
while(t--){
    cin>>n;
    c4=0;c7=0;
    if(n.length()==1){
        if(n=="4"||n=="7"){
            cout<<"1"<<endl;
        }
        else cout<<"2"<<endl;
    }
    else{
        for(int i=0;i<n.length();i++){
            if(n[i]=='4') c4++;
            else if(n[i]=='7') c7++;
        }
        if(c4+c7==n.length()) cout<<"0"<<endl;
        else{
            diff=n.length()-(c4+c7);
            cout<<diff<<endl;
        }
    }
}
}
