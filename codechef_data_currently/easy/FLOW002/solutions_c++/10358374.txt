#include<iostream>
using namespace std;
int main(){
int t,a,b,div,rem;
cin>>t;
for(int i=0;i<t;i++){
    cin>>a>>b;
    div=a/b;
    rem=a-(b*div);
    cout<<rem<<endl;
}
}
