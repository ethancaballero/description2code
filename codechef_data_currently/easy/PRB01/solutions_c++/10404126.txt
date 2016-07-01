#include<iostream>
using namespace std;
int checkprime(int);
int main(){
int t,n;
cin>>t;
while(t--){
    cin>>n;
    checkprime(n);
}
}
int checkprime(int a){
int r,p=0;
if(a>2){
    for(int i=2;i<a;i++){
        r=a%i;
        if(r==0){p=0;break;}
        else {p=1;}
    }

}
if(a==0||a==1) p=0;
if(a==2) p=1;
if(p==0){cout<<"no"<<endl;}
else cout<<"yes"<<endl;
}
