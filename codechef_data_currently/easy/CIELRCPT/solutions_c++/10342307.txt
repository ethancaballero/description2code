#include<iostream>
#include<math.h>
using namespace std;
int findnear(int);
int main(){
int t,p,near,f=0;
cin>>t;
for(int i=0;i<t;i++){
    cin>>p;
    f=0;
    for(int j=0;p!=0;j++){
    near=findnear(p);
    p=p-near;
    f+=1;
    if(p==0) break;
    }
    cout<<f<<endl;
}
} //END OF MAIN

int findnear(int x){
int y=1, z=0;
if(x<=2048){
    while(x>=y){
        z+=1;
        y=pow(2.0,z);
    }
    y=pow(2.0,z-1);
}
else y=2048;
return y;
}
