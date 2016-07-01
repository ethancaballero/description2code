#include<iostream>
using namespace std;
int main(){
int t,c,min;
string m,w;
cin>>t;
while(t--){
    cin>>m>>w;
    /*size_t pos = m.find(w);
    size_t pos2 = w.find(m);
    if(pos==string::npos && pos2==string::npos) cout<<"NO"<<endl;
    else cout<<"YES"<<endl;*/
    min=0;c=0;
    if(m.length()>w.length()){
        for(int i=0;i<w.length();i++){
            for(int j=min;j<m.length();j++){
                if(m[j]==w[i]) {c++;min=j+1;break;}
        }
    }
    if (c==w.length()) cout<<"YES"<<endl;
    else cout<<"NO"<<endl;
    }
        else if(w.length()>=m.length()){
        for(int i=0;i<m.length();i++){
            for(int j=min;j<w.length();j++){
                if(m[i]==w[j]) {c++;min=j+1;break;}
        }
    }
    if (c==m.length()) cout<<"YES"<<endl;
    else cout<<"NO"<<endl;
    }
}
}
