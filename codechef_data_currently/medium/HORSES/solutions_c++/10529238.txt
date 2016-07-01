#include<iostream>
#include<algorithm>
using namespace std;
int main(){
int t,n,least;
cin>>t;
while(t--){
    cin>>n;
    long int s[n];
    for(int i=0;i<n;i++){
        cin>>s[i];
    }
    sort(s,s+n);
    least=s[n-1];
    for(int i=0;i<n-1;i++){
        if(s[i+1]-s[i]<least){
            least=s[i+1]-s[i];
        }
    }
    cout<<least<<endl;
}
}
