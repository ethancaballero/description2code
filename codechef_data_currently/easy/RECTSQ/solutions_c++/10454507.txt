#include<iostream>
#include<math.h>
using namespace std;
int main(){
int t,n,m,low,div,area,sq;
cin>>t;
while(t--){
    cin>>n>>m;
    if(n>m) low=m;
    else low=n;
    for(int i=1;i<=low;i++){
        if(m%i==0 && n%i==0) div=i;
    }
    div=pow(div,2.0);
    area=m*n;
    sq=area/div;
    cout<<sq<<endl;
}
}
