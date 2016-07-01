#include<iostream>
using namespace std;
int main(){
long long int a;
cin>>a;
if(a==0) cout<<"yes"<<endl;
else if((a-1)%6==0) cout<<"yes"<<endl;
else if((a-3)%6==0) cout<<"yes"<<endl;
else if ((a-6)%6==0) cout<<"yes"<<endl;
else cout<<"no"<<endl;
}
