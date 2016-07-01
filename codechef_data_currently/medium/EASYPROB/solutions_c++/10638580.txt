#include <iostream>
using namespace std;
 
inline string cvt(int n)
{
	if(n==1)
		return "2(0)";
		
	int i=0;
	while((1<<i)<=n)
		i++;
	i--;
	
	string s="2";
	if(i>1)
		s+="("+cvt(i)+")";
	if(n-(1<<i))
		s+="+"+cvt(n-(1<<i));
	
	return s;
}
 
int main()
{
	int i,a[]={137,1315,73,136,255,1384,16385};
	for(i=0;i<6;i++)
		cout<<a[i]<<"="<<cvt(a[i])<<endl;
	cout<<a[i]<<"="<<cvt(a[i]);
	return 0;
} 