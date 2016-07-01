#include<iostream>
using namespace std;
int main(){
int t,n,current,previous,c;
cin>>t;
while(t--){
    cin>>n;
    long long int ans=0;
    for(int i=0;i<n;i++){
        cin>>current;
        if(i==0) c=1;
        else {
            if(current>=previous)
                ++c;
            else
                c=1;
        }
    ans+=c;
    previous=current;
    }
cout<<ans<<endl;
}
}
