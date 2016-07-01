#include<iostream>
using namespace std;
int main(){
int t,act,pos,severity,laddus,months;
cin>>t;
while(t--){
    laddus=0;
    string origin,act_name;
    cin>>act;
    cin>>origin;
    for(int i=0;i<act;i++){
        cin>>act_name;
        if(act_name=="CONTEST_WON"){
            cin>>pos;
            if(pos<=20) laddus+=(300+(20-pos));
            else laddus+=300;
        }
        else if(act_name=="BUG_FOUND"){
                cin>>severity;
                laddus+=severity;
        }
        else if(act_name=="TOP_CONTRIBUTOR") laddus+=300;
        else if(act_name=="CONTEST_HOSTED") laddus+=50;
    }
    if(origin=="INDIAN") months=laddus/200;
    else if(origin=="NON_INDIAN") months=laddus/400;
    cout<<months<<endl;
}
}
