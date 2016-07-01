#include<iostream>
#include<algorithm>
using namespace std;
int main(){
int t,n,k,e;
long long int m,score,smark,min;
cin>>t;
while(t--){
    cin>>n>>k>>e>>m;
    long long int marks[n-1];
    for(int i=0;i<n-1;i++){
        marks[i]=0;
        for(int j=0;j<e;j++){
            cin>>score;
            marks[i]+=score;
        }
    }
    smark=0;
    for(int i=0;i<e-1;i++){
        cin>>score;
        smark+=score;
    }
sort(marks,marks+(n-1));
min=(marks[n-k-1]+1)-smark;
if(min>m) cout<<"Impossible"<<endl;
else{
    if(min<0) cout<<"0"<<endl;
    else cout<<min<<endl;
}
}
}
