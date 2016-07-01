#include<iostream>
using namespace std;
int main(){
std::ios::sync_with_stdio(false);
int n,k;
long int a;
cin>>a>>n>>k;
int nuke[105]={0},f=0;
n+=1;
for(int i=0;i<k;i++){
    nuke[i]=a%n;
    a=a/n;
    cout<<nuke[i]<<" ";
}
cout<<endl;
}
