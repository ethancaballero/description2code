#include<iostream>
using namespace std;
int main(){
int t,n;
cin>>t;
string ans1,ans2,ans3;
while(t--){
    cin>>n;
    if(n<=360){
        if(360%n==0) ans1="y";
        else ans1="n";
        ans2="y";
        if((n*(n+1)/2)<360) ans3="y";
        else ans3="n";
    }
    else{
        ans1="n";
        ans2="n";
        ans3="n";
    }
    cout<<ans1<<" "<<ans2<<" "<<ans3<<endl;
}
}
