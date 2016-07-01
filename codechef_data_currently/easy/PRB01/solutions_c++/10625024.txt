#include<bits/stdc++.h>
using namespace std;
int main()
{
	int t;
	cin>>t;
	while(t--)
	{
		int i,flag=0,num;
		cin>>num;
		for(i=2;i<=num/2;i++)
		{
			if(num%i==0)
			{
				flag=1;
				break;
			}
		}
		if(flag==0)
		cout<<"yes"<<endl;
		else
		cout<<"no"<<endl;
	}
}
