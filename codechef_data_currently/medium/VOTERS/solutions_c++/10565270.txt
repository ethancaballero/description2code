#include<iostream>
using namespace std;
int main(){
int n1,n2,n3,c,num;
cin>>n1>>n2>>n3;
int d;
int n=n1+n2+n3;
int fin[1000000];
int a[1000000];
for(int i=0;i<1000000;i++){
    a[i]=0;
}
while(n--){
    cin>>num;
    a[num]++;
}
c=0;
for(int i=0;i<1000000;i++){
    if(a[i]>1) c++;
}
cout<<c<<endl;
for(int i=0;i<1000000;i++){
    if(a[i]>1) cout<<i<<endl;
}
}
