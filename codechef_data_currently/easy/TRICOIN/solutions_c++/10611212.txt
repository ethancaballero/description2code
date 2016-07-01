#include<bits/stdc++.h>

using namespace std;

int main(){
int T;
cin>>T;
while(T--){
    	long long N,count=0,a,d,i;
    	cin>>N;
    	i=0;
    	while(N>0){
                a=1+(i);
                N-=a;
                if(N>=0){
                    count++;
                }
                i++;
    	}
    	cout<<count<<endl;
}
return 0;
}
