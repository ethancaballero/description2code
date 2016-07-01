#include<iostream>
using namespace std;
int main(){
ios::sync_with_stdio(false);
int t,n,c,q,l,r,x;
cin>>t;
while(t--){
    cin>>n>>c>>q;
    for(int i=0;i<q;i++){
        cin>>l>>r;
        if(l<=c && r>=c){
            //cout<<"Satisfied outer if"<<endl;
            if((c-l)<(r-c)){
                x=c-l;
                c=r-x;
                //cout<<"Current pos="<<c<<endl;
            }
            else if((r-c)<(c-l)){
                x=r-c;
                c=l+x;
                //cout<<"Current pos="<<c<<endl;
            }
        }
    }
    cout<<c<<endl;
}
}
