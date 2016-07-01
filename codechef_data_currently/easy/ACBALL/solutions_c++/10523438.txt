#include<iostream>
using namespace std;
int main(){
int t;
cin>>t;
while(t--){
    string x,y,hd;
    cin>>x>>y;
    for(int i=0;i<x.length();i++){
        if(x[i]==y[i]){
            if(x[i]=='B') hd='W';
            else hd='B';
        }
        else if(x[i]=='B' && y[i]=='W') hd='B';
        else if(x[i]=='W' && y[i]=='B') hd='B';

        cout<<hd;
    }
    cout<<endl;
}
}
