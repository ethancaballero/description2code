#include<bits/stdc++.h>
using namespace std;

int main(){
long T;
cin>>T;
while(T--){
    char ch;
    cin>>ch;
    if(ch=='B' || ch=='b'){
        cout<<"BattleShip";
    }
    else if(ch=='C' || ch=='c'){
        cout<<"Cruiser";
    }
    else if(ch=='D' || ch=='d'){
        cout<<"Destroyer";
    }
    else if(ch=='F' || ch=='f'){
        cout<<"Frigate";
    }
    cout<<endl;
}
return 0;
}

