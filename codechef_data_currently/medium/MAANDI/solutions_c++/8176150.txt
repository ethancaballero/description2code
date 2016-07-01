#include<bits/stdc++.h>
using namespace std;

bool olchk(int n)
{
    int r;
    while(n)
    {
        r=n%10;
        n=n/10;
        if(r==4||r==7)return 1;
    }
    return 0;
}

int main()
{
    ios_base::sync_with_stdio(0);
    int t,n,r,i,j;
    cin>>t;
    while(t--)
    {
        r=0;
        cin>>n;
        for(i=1;i<sqrt(n);i++)
        {

            if(n%i==0)
            {
                if(olchk(i))r++;
                if(olchk(n/i))r++;
            }

        }
        if((float)sqrt(n)==(int)sqrt(n))
        {

            if(olchk(sqrt(n)))r++;
        }
        cout<<r<<endl;
    }
    return 0;
}
