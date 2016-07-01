#include<bits/stdc++.h>
using namespace std;

struct par
{
	int x;
	int y;
	int d;
}a[31];

bool asc(par a,par b)
{
	return (a.d<b.d);
}

int main()
{
	
	ios_base::sync_with_stdio(0);
	int t,n,k,i,j;
	cin>>t;
	while(t--)
	{
		char s[2001]={0};
		cin>>n>>k;
		for(i=0;i<k;i++)
		{
			cin>>a[i].x>>a[i].y;
			a[i].d=a[i].y-a[i].x;
			s[a[i].x]='(';
			s[a[i].y]=')';
		}
		sort(a,a+k,asc);
		for(i=0;i<k;i++)
		{
			int c=1;
			for(j=a[i].x+1;j<a[i].y;j++)
			{
				
				
				if(s[j]==0)
				{
					if(c>0)
					{
						s[j]=')'; 
						c--;
					}
					else
					{
						s[j]='(';
						c++;
					}
				}
				
				else
				{
					if(s[j]=='(')c++;
					else c--;
				}
				
			}
	         }
			for(i=0;i<n;i++)
			{
				if(s[i]==0)
				{
					s[i]=')';
				}
				cout<<s[i];
			}
			cout<<endl;

	}
	return 0;

}