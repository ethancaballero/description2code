#include<iostream>
using namespace std;
int main(){
int t,s;
double hra,da,total;
cin>>t;
while(t--){
    cin>>s;
    if(s<1500){
        hra=(0.1)*s;
        da=(0.9)*s;
    }
    else if(s>=1500){
        hra=500;
        da=(0.98)*s;
    }
    total=s+hra+da;
    cout<<total<<endl;

}
}
