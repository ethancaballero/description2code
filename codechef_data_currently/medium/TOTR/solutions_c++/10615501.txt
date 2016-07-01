#include<iostream>
#include<ctype.h>
using namespace std;
int main(){
int t;
char map[27], s[101];
cin>>t>>map;
while(t--){
    cin>>s;
    for(int i=0;s[i];i++){
        if(islower(s[i])) s[i] = map[s[i] - 'a'];
        else if(isupper(s[i])) s[i] = toupper(map[s[i] - 'A']);
        else if(s[i]=='_') s[i]=' ';
    }
    cout<<s<<endl;
}
}
