#include<bits/stdc++.h>
using namespace std;
int main()
{
	int n,loc1,loc2,i,x1,y1,x2,y2,x3,y3;
	long long int min,max,area;
	scanf("%d",&n);
	for(i=0;i<n;i++)
	{
		scanf("%d%d%d%d%d%d",&x1,&y1,&x2,&y2,&x3,&y3);
		area = abs(x1*(y2-y3)+ x2*(y3-y1) + x3*(y1-y2));
		if(i == 0)
		{
			max = area;
			min = area;
			loc1 = i;
			loc2 = i;
		}
		else{
			if(area >= max)
			{
				if(max == min && max == area)
				{
					loc1 = i;
					loc2 = i;
				}
				max = area;
				loc1 = i;
			}
			else if(area <= min)
			{
				min = area;
				loc2 = i;
			}
		}
		
	}
	printf("%d %d",loc2 +1,loc1 +1);
return 0;
}