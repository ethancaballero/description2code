#include<iostream>
using namespace std;
int main(){
int t,n;
cin>>t;
while(t--){
    cin>>n;
    int l[n],r[n],s,sum=0,index,rtrack;
    for(int i=0;i<n;i++){
        cin>>l[i];
    }
    for(int i=0;i<n;i++){
        cin>>r[i];
    }
    for(int j=0;j<n;j++){
        s=l[j]+r[j];
        if(s>sum){
            index=j;
            rtrack=r[j];
            sum=s;
        }
        else if(s==sum){
            if(r[j]>rtrack){
                index=j;
                rtrack=r[j];
                sum=s;
            }
        }
    }
    cout<<index+1<<endl;
}
}
