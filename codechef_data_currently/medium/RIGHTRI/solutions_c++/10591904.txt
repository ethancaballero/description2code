#include<iostream>
#include<algorithm>
using namespace std;
double slope(int,int,int,int);
int main(){
int n,x1,y1,x2,y2,x3,y3;
long int d1,d2,d3;
cin>>n;
int c=0;
while(n--){
    cin>>x1>>y1;
    cin>>x2>>y2;
    cin>>x3>>y3;
    d1=((x2-x1)*(x2-x1))+((y2-y1)*(y2-y1));
    d2=((x3-x2)*(x3-x2))+((y3-y2)*(y3-y2));
    d3=((x3-x1)*(x3-x1))+((y3-y1)*(y3-y1));
    int pythagoras[3]={d1,d2,d3};
    sort(pythagoras,pythagoras+3);
    if(pythagoras[2]==(pythagoras[0]+pythagoras[1])) c++;
}
cout<<c<<endl;
}
