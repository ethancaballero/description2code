#include<iostream>
using namespace std;
int main(){
std::ios::sync_with_stdio(false);
int n,k;
long int a;
cin>>a>>n>>k;
int nuke[105]={0},f=0;
for(int i=0;i<a;i++){
    nuke[0]+=1;
    for(int j=0;true;j++){
        if(nuke[j]>n){
            nuke[j+1]+=1;
            nuke[j]=0;
        }
        else break;
    }
}
for(int x=0;x<k;x++){
cout<<nuke[x]<<" ";
}
cout<<endl;
}
