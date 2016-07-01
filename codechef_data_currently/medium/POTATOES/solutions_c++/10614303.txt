//Reduced the complexity by decreasing the number of inner loops from n/2 to sqrt(n)
#include<iostream>
#include<math.h>
using namespace std;
int main(){
int t,x,y,z,sum,flag,sq;
cin>>t;
while(t--){
    cin>>x>>y;
    sum=x+y;
    for(int i=sum+1;true;i++){
        flag=0;
        sq=sqrt(i);
        for(int j=2;j<=sq;j++){
            if((i%j)==0) {flag=1;break;}
        }
        if(flag==0) {z=i;break;}
    }
    cout<<z-sum<<endl;
}
}
