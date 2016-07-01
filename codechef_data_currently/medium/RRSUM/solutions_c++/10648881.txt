#include<iostream>
using namespace std;
int main(){
ios::sync_with_stdio(false);
long long int n,m,q,mins,maxs;
cin>>n>>m;
mins=n+2;
maxs=n*3;
for(int i=0;i<m;i++){
    cin>>q;
    if(q>=mins && q<=maxs){
        cout<<min(q-mins,maxs-q)+1<<endl;
    }
    else cout<<"0"<<endl;
}
}
