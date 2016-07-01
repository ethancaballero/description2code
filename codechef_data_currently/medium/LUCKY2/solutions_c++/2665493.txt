#include <iostream>  
#include <sstream>  
#include <cstdio>  
#include <cstdlib>  
#include <cmath>  
#include <memory>  
#include <cctype>  
#include <string>  
#include <vector>  
#include <list>  
#include <queue>  
#include <deque>  
#include <stack>  
#include <map>  
#include <set>  
#include <algorithm>  
using namespace std; 
  
#define FOR(i,a,b) for(int (i) = (a); (i) < (b); ++(i)) 
#define RFOR(i,a,b) for(int (i) = (a)-1; (i) >= (b); --(i)) 
#define CLEAR(a) memset((a),0,sizeof(a)) 
#define INF 1000000000 
#define PB push_back 
#define ALL(c) (c).begin(), (c).end() 
#define pi 2*acos(0.0) 
#define SQR(a) (a)*(a) 
#define MP make_pair 
#define MOD 1000000007
#define MAX 10010
typedef long long Int; 
 
 
int t, l;
string a, b, s;
vector <int> L;
int F1[MAX];
int F2[MAX];
 
void Gen(int x)
{
		if (x > 0)
				L.PB(x);
		if (x < 1000)
		{
				Gen(x*10 + 4);
				Gen(x*10 + 7);
		}
}
 
int Pow(int a, int p)
{
		int res = 1;
		while (p > 0)
				if (p % 2 == 0)
				{
						p /= 2;
						a = (int)(((Int)a * (Int)a) % MOD);
				}
				else
				{
						p--;
						res = (int)(((Int)res * (Int)a) % MOD);
				}
		return res;
}
 
int C(int a, int b)
{
		if (b > a)
				return 0;
		if (b < 0)
				return 0;
 
		Int res = F1[a];
		res *= F2[b];
		res %= MOD;
 
		res *= F2[a-b];
		res %= MOD;
 
		return (int)res;
}
 
int Count(int c, int k)
{
		k = l-k;
		if (k < 0)
				return 0;
		if (c < k)
				return 0;
		Int res = Pow(2, k);
		res = res * C(c, k);
		res %= MOD;
		res = res * Pow(8, c-k);
		res %= MOD;
 
		return res;
}
 
int F(int pos, int k)
{
		if (k > l)
				return 0;
		if (pos == s.size())
		{
				if (k == l)
						return 1;
				return 0;
		}
		int res = 0;
		FOR (i,'0',s[pos])
		{
				res += Count(s.size()-pos-1, k + (i == '4' || i == '7'));
				res %= MOD;
		}
 
		res += F(pos+1, k + (s[pos] == '4' || s[pos] == '7'));
		res %= MOD;
 
		return res;
}
 
int main()
{
		Gen(0);
		sort(ALL(L));
 
		F1[0] = 1;
		F2[0] = Pow(F1[0], MOD-2);
 
		FOR (i,1,MAX)
		{
				F1[i] = (int)(((Int)F1[i-1] * (Int)i) % MOD);
				F2[i] = Pow(F1[i], MOD-2);
		}
 
		cin >> t;
		FOR (tt,0,t)
		{
				cin >> a >> b;
				int cnt = 0;
				FOR (i,0,a.size())
						if (a[i] == '4' || a[i] == '7')
								cnt++;
 
				int res = 0;
				FOR (i,0,L.size())
				{
						l = L[i];
						s = b;
						res += F(0, 0);
						res %= MOD;
						s = a;
						res -= F(0, 0);
						if (res < 0)
								res += MOD;
						res %= MOD;
						if (L[i] == cnt)
								res++;
						res %= MOD;
				}
				cout << res << endl;
		}
		return 0;
} 
   