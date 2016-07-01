#include<iostream>
using namespace std;
int main()
{
   int n;
   cin>>n;
   int p1,p2,m=0,c=0,d=0,e;
   for(int i=0;i<n;i++)
   {
       cin>>p1>>p2;
       c+=p1;
       d+=p2;
       if(c>d && m<c-d)
       {
          m=c-d;
          e=1;
       }
       else if(c<d && m<d-c)
        {
           m=d-c;
           e=2;
        }
   }

       cout<<e<<" "<<m;

}
