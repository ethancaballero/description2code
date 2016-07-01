#include<iostream>
#include<math.h>
using namespace std;
int main(){
int t,n,m;
cin>>t;
while(t--){
    cin>>n>>m;
    int note[n];
    for(int i=0;i<n;i++){
        cin>>note[i];
    }
    for(int i=0;i<pow(2,n);i++){
        int sum=0;
        for(int j=0;j<n;j++){
            if(i&(1<<j)){
                sum+=note[j];
            }
        }
        if(sum==m){
            cout<<"Yes"<<endl;
            break;
        }
        else if(i==(pow(2,n)-1))
            cout<<"No"<<endl;
    }
}
}
