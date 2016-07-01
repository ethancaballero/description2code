#include <bits/stdc++.h>
using namespace std;

#define g(n) scanf("%d",&n)
// #define g(n) inp(n)
#define gl(n) scanf("%lld", &n)
#define f(i,n) for(int i=0; i<n; i++)
#define pb push_back
#define mp make_pair
#define fab(i,a,b) for(int i=a; i<=b; i++)
#define test(t) while(t--)
#define getcx getchar//_unlocked

typedef long long int ll;
typedef pair<int,int> pii;
typedef vector<int> vi;
typedef vector< vi > vvi;

void print(char ch, int c)
{
	while(c--)
		cout << ch;
}

int main()
{
	char str[100005];
	int t,n,k;
	cin >> t;
	while(t--)
	{
		cin >> n >> k;
		cin >> str;
		assert(strlen(str) == n);
		vi count(0);
		int cnt = 1;
		char start = str[0];
		char prev = str[0];

		for(int i=1; i<n; i++)
		{
			if(str[i] == prev)
				cnt++;
			else
			{
				count.pb(cnt);
				prev = str[i];
				cnt = 1;
			}
		}
		count.pb(cnt);
		// cout << "count ";
		// f(i,count.size())
		// {
		// 	cout << count[i] << " ";
		// }
		// cout<<endl;

		if(k == 1)
		{
			int swapsIfFirstZero = 0, swapsIfFirstOne = 0;
			for(int i=0; i<n; i++)
			{
				if(str[i] == '0')
				{
					if(i%2 == 0) //zero at even pos
						swapsIfFirstOne++;
					else
						swapsIfFirstZero++;
				}
				else
				{
					if(i&1)
						swapsIfFirstOne++;
					else
						swapsIfFirstZero++;
				}
			}
			
			char start = '1';
			int swaps = swapsIfFirstOne;

			if(swapsIfFirstZero < swapsIfFirstOne)
			{
				start = '0';
				swaps = swapsIfFirstZero;
			}

			char other = start == '1' ? '0' : '1';
			cout << swaps << endl;
			for(int i=0; i<n; i++)
			{
				if(i&1)
					cout << other;
				else
					cout << start;
			}
			cout << endl;
			continue;
		}

		int swaps = 0;
		vi ans(0);
		for(int i=0; i<count.size();i++)
		{
			if(count[i]<=k)
			{
				ans.pb(count[i]);
			}
			else if((count[i] % (k+1)) == 0)
			{
				int newSwaps = count[i]/(k+1);
				swaps+=newSwaps;
				ans.pb(k-1);
				ans.pb(1);
				for(int j=1; j<newSwaps; j++)
				{
					ans.pb(k);
					ans.pb(1);
				}
				ans.pb(1);
			}
			else
			{
				int newSwaps = count[i]/(k+1);
				swaps += newSwaps;
				
				for(int j=0; j<newSwaps; j++)
				{
					ans.pb(k);
					ans.pb(1);
				}
				ans.pb(count[i]%(k+1));
			}
		}
		cout << swaps << endl;
		char other = start=='1'? '0':'1';
		for(int i=0; i<ans.size(); i++)
		{
			if(i&1)
				print(other, ans[i]);
			else
				print(start, ans[i]);
		}
		cout << endl;
	}
	return 0;
}