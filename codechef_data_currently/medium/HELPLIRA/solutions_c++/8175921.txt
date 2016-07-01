#include<bits/stdc++.h>
using namespace std;
 
int main()
{
    int n,i,r,p,x1,x2,x3,y1,y2,y3;
    int a=0,m,b=INT_MAX;
    cin>>n;

    for(i=0;i<n;i++)

    {
 
        cin>>x1>>y1>>x2>>y2>>x3>>y3;
        m=fabs(x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2));
        if(m>=a){a=m;r=i+1;}
        if(m<=b){b=m;p=i+1;}
    }
    cout<<p<<" "<<r;
    return 0;
}

