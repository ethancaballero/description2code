#include<iostream>
using namespace std;
int main(){
int t,c;
long int a,b;
cin>>t;
while(t--){
    cin>>a>>b;
    c=0;
    while(a!=b){
        if(b%a==0) a=2*a;
        else{
            if(a%2==0)
                a=a/2;
            else
                a=(a-1)/2;
        }
        c++;
    }
    cout<<c<<endl;
    }
}
