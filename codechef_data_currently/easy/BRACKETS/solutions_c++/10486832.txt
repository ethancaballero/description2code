#include<iostream>
using namespace std;
int main(){
int t,balance,max_balance;
cin>>t;
string s;
while(t--){
cin>>s;
balance=0;
max_balance=0;
for(int i=0;i<s.length();i++){
    if(s[i]=='(') balance+=1;
    if(s[i]==')') balance-=1;
    if(balance>max_balance) max_balance=balance;
}
for(int j=0;j<max_balance;j++){
    cout<<'(';
}
for(int j=0;j<max_balance;j++){
    cout<<')';
}
cout<<endl;
}
}
