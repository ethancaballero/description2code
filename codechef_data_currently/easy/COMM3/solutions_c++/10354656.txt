#include<iostream>
#include<math.h>
using namespace std;
double distance(int,int,int,int);
int check(int,double,double,double);
int main(){
int t,r,cx,cy,hx,hy,sx,sy;
double d1,d2,d3;
cin>>t;
for(int i=0;i<t;i++){
    cin>>r;
    cin>>cx>>cy;
    cin>>hx>>hy;
    cin>>sx>>sy;
    d1=distance(cx,hx,cy,hy);
    d2=distance(hx,sx,hy,sy);
    d3=distance(cx,sx,cy,sy);
    check(r,d1,d2,d3);
}
}
double distance(int x1,int x2,int y1,int y2){
double d;
d=sqrt(pow((x2-x1),2.0)+pow((y2-y1),2.0));
return d;
}
int check(int x,double p,double q,double r){
int f=0;
if(x>=p) f+=1;
if(x>=q) f+=1;
if(x>=r) f+=1;
if(f>=2) cout<<"yes"<<endl;
else cout<<"no"<<endl;
}
