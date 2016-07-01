#include<iostream>
using namespace std;
int main(){
int t,l,r,x,la,rev;
cin>>t;
while(t--){
    cin>>l>>r;
    long int sum=0;
    for(int i=l;i<=r;i++){
        x=i;
        rev=0;
        for(int j=0;x>0;j++){
            la=x%10;
            rev=(rev*10)+la;
            x=x/10;
        }
        if(i==rev) sum+=i;
    }
    cout<<sum<<endl;
}
}
