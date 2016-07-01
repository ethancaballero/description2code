#include<iostream>
#include<math.h>
using namespace std;
int main(){
int t;
cin>>t;
while(t--){
   long long int s,dis,sol;
    cin>>s;
    dis=sqrt(1+(8*s));
    sol=(dis-1)/2;
    cout<<sol<<endl;
}
}
