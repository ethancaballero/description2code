#include<bits/stdc++.h>
using namespace std;



long long int Xor(int x1,int y1,int x2,int y2,int a[71][71])
{
    return(a[x2][y2]^a[x1-1][y2]^a[x2][y1-1]^a[x1-1][y1-1]);
}

int main()
{
    ios_base::sync_with_stdio(0);
    int t,n,i,j,i1,j1,x1,y1,x2,y2;
    long long int m;
    cin>>t;
    while(t--)
    {
        m=0;
        cin>>n;
        int b[71][71]={0};
        int a[71][71]={0};
            
        for(i=1;i<=n;i++)
            for(j=1;j<=n;j++)
            cin>>b[i][j];

        for(i1=1;i1<=n;i1++)
            for(j1=1;j1<=n;j1++)
        for(i=1;i<=i1;i++)
            for(j=1;j<=j1;j++)
            a[i1][j1]^=b[i][j];

         for(x1=1;x1<=n;x1++)
            for(y1=1;y1<=n;y1++)
        for(x2=x1;x2<=n;x2++)
            for(y2=y1;y2<=n;y2++)
            m=max(m,Xor(x1,y1,x2,y2,a));
            cout<<m<<endl;
    }
    return 0;
}
