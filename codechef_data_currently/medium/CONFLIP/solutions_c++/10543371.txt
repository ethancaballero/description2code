//Optimal Solution - Program does NOT perform the flipping and counting.
#include<iostream>
using namespace std;
int main(){
int t,state,g,q;
long int n;
cin>>t;
while(t--){
    cin>>g;
    for(int i=0;i<g;i++){
        cin>>state>>n>>q;
        long int c;
        if((n%2)==1){
            if(state==1) state=2;
            else if(state==2) state=1;
            if(q==state) c=(n/2)+1;
            else c=n/2;
        }
        else if(n%2==0){
            c=n/2;
        }
        cout<<c<<endl;
    }
}
}
