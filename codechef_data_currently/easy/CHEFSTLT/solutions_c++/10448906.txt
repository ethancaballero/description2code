#include<iostream>
using namespace std;
int main(){
int t,c,low,high;
string s1,s2;
cin>>t;
while(t--){
    cin>>s1>>s2;
    c=0;low=0;high=0;
    for(int i=0;i<s1.length();i++){
        if(s1[i]==s2[i] && !(s1[i]=='?') && !(s2[i]=='?')) c+=1;
        if(s1[i]=='?' && s2[i]=='?') low+=1;
        if((s1[i]=='?' && !(s2[i]=='?'))||(!(s1[i]=='?') && s2[i]=='?')) low+=1;
    }
    low=(s1.length())-(low+c);
    high=(s1.length())-c;

    cout<<low<<" "<<high<<endl;
}
}
