#include <iostream>
#include <stdio.h>
#include <string.h>
using namespace std;
#define REP(i,a,b) for(i=a;i<b;i++)
#define rep(i,n) REP(i,0,n)


int main()
{
	bool conversion_matrix[10][10]={
									{true ,false,false,false,false,false,false,false,true ,false},//0
									{true ,true ,false,true ,true ,false,false,true ,true ,true },//1
									{false,false,true ,false,false,false,false,false,true ,false},//2
									{false,false,false,true ,false,false,false,false,true ,true },//3
									{false,false,false,false,true ,false,false,false,true ,true },//4
									{false,false,false,false,false,true ,true ,false,true ,true },//5
									{false,false,false,false,false,false,true ,false,true ,false},//6
									{true ,false,false,true ,false,false,false,true ,true ,true },//7
									{false,false,false,false,false,false,false,false,true ,false},//8
									{false,false,false,false,false,false,false,false,true ,true }//9
								};
	char digits_of_s[10],digits_of_m[10];

	int t,S,M,i=0,j=0,k=0;
	int temp=0;
	cin>>t;
	while(t--)
	{
		cin>>S;
		cin>>M;
		sprintf(digits_of_s,"%d",S);
		sprintf(digits_of_m,"%d",M);
		int digs=strlen(digits_of_s);
		int digm=strlen(digits_of_m);
		rep(i,digs) digits_of_s[i] -= '0';
		rep(i,digm) digits_of_m[i] -= '0';
		//cout<<digs<<" "<<digm<<endl;
		int fit = 0, mx = -1,next_fit =-1, next_mx = -1;
		/* fit = the current maximum value which has the only same digits of M */
		/* mx  = the current maximum value other than above case */
		int res = S;
		rep(k,digm-digs+1)
		{
			 /* k = where is the first letter of S */
			fit = 0; mx = -1;
			/* fit = the current maximum value which has the only same digits of M */
			/* mx  = the current maximum value other than above case */
			rep(i,digm)
			{
				next_fit = next_mx = -1;
				rep(j,10)
				{
					/* checking about i-th degits (from left) = j */
					if(0<=i-k&&i-k<digs && conversion_matrix[digits_of_s[i-k]][j]==false) {continue; /* Can this digit be changed to j? */}
					if(next_mx < mx*10 + j)
					{
						next_mx = mx*10 + j;
						
					}
					if(j <  digits_of_m[i] && next_mx  < fit*10 + j)
					{
						next_mx  = fit*10 + j;
					}
					if(j == digits_of_m[i] && next_fit < fit*10 + j)
					{
						next_fit = fit*10 + j;
					}
					//if(S==10381){cout<<next_mx<<" "<<next_fit<<endl;}
				}
				fit = next_fit;
				mx  = next_mx;
				if(i-k >= digs-1 && res < fit) res = fit;
				if(i-k >= digs-1 && res < mx)  res = mx;
			}
		}
		cout<<res<<endl;
	}
return 0;
}
