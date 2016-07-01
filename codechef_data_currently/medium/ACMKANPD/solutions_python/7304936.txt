#include<iostream>
#include<string>
using namespace std;
int main()
{
    string str;
    while(1)
    {
    cin>>str;
    if(str=="~")break;
    char flag='0';
    string ans="3";
    while(1)
     {  
       if(str=="#") break;
       
     int c=str.size();
      if(c==1) flag='1';
      else if(c==2) flag='0';
      else
      {
            c-=2;
            for(int i=0;i<c;i++)
            ans+=flag;
      }
      cin>>str; 
     }
     int a=0;
     int c=ans.size();
     int p=1, sum=0;
     for(int i=0;i<c;i++)
     {
                    
                     if(ans[c-1-i]=='1')sum+=p;
                      p<<=1;
     }
     cout<<sum<<endl;
    }
}