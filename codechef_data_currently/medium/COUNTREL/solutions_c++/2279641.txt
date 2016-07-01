#include <iostream>
#include "stdio.h"
using namespace std;

long long int power(long long int x, long long int y)
{
    long long int temp;
    if( y == 0)
        return 1;
    temp = power(x, y/2)%100000007;
    if (y%2 == 0)
        return (temp*temp)%100000007;
    else
        return (((x*temp)%100000007)*temp)%100000007;
}




int main(int argc, char const *argv[])
{
	int Testcases;
	scanf("%d",&Testcases);
	for(int z = 0;z<Testcases;z++)
	{
		long long int x, fx, gx;
		cin >> x;
		fx = (((power(3,x)+1)*50000004)%100000007 - power(2,x))%100000007;
		fx = (fx+100000007)%100000007;
		gx = (2*power(4,x-1) - power(3,x) + power(2,x-1) + power(2,x) - ((power(3,x)+1)*50000004)%100000007)%100000007;
		gx = (gx+100000007)%100000007;
		cout<<fx<<" "<<gx<<endl;

	}
	return 0;
} 