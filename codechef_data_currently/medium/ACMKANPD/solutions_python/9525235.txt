#include <iostream>
#include <string>

using namespace std;

int main(int argc, char const *argv[])
{
	int flag = 0, l = 0, num = 0;
	string temp;

	while(1)
	{
		cin>>temp;
		if(temp[0] != '#')
		{
			l = temp.length();
			if(l == 1)
				flag = 1;
			else if(l == 2)
			{
				flag = 0;
				continue;
			}
			else
			{
				while(l-2 > 0)
				{
					num = num << 1;
					num = num|flag;
					l--;
				}
				continue;
			}

			if(temp[0] == '~')
				return 0;
		}
		else
		{
			cout<<num<<endl;
			num = 0;
		}
	}

	return 0;
}