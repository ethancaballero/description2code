#include<iostream>
#include<iomanip>
using namespace std;
int main(){
int t,q,p;
double total,dis;
cin>>t;
for(int i=0;i<t;i++){
    cin>>q>>p;
    if(q<=1000){
        total=q*p;
    }
    else {
        total=0.9*q*p;
    }
    cout<<fixed<<setprecision(6)<<total<<endl;
}
}
