#include<iostream>
using namespace std;
int main(){
std::ios::sync_with_stdio(false);
int t,n,s;
cin>>t;
while(t--){
    int c=0,prev=0;
    cin>>n;
    for(int i=0;i<n;i++){
        cin>>s;
        if(i==0){c++;prev=s;}
        else {
        if(s<=prev){c++;prev=s;}
        }
    }
    cout<<c<<endl;
}
}
