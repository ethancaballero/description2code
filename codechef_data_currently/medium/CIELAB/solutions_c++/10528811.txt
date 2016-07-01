#include<iostream>
#include<algorithm>
using namespace std;
int main(){
int a,b,sub;
cin>>a>>b;
sub=abs(a-b);
if(sub==1) sub=2;
else if(sub%10==0) sub=sub+1;
else sub=sub-1;
cout<<sub<<endl;
}
