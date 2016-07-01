#include<iostream>
using namespace std;
int main(){
int n,a,lucky=0,unlucky=0;
cin>>n;
for(int i=0;i<n;i++){
    cin>>a;
    if(a%2==0) lucky++;
    else unlucky++;
}
if(lucky>unlucky) cout<<"READY FOR BATTLE"<<endl;
else cout<<"NOT READY"<<endl;
}
