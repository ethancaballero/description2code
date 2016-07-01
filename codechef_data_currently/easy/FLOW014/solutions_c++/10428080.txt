#include<iostream>
using namespace std;
int main(){
int t,grade;
double hard,carbon,tensile;
cin>>t;
while(t--){
    cin>>hard>>carbon>>tensile;
    if(hard>50 && carbon<0.7 && tensile>5600) grade=10;
    else if(hard>50 && carbon<0.7 && tensile<=5600) grade=9;
    else if(hard<=50 && carbon<0.7 && tensile>5600) grade=8;
    else if(hard>50 && carbon>=0.7 && tensile>5600) grade=7;
    else if(hard<=50 && carbon>=0.7 && tensile<=5600) grade=5;
    else grade=6;
    cout<<grade<<endl;
}
}
