using namespace std;

#include "bits/stdc++.h"

typedef long long LL;

LL A[100005];

LL P[100005];

LL getPow(LL a, LL b) {
	LL res = 1;
	while(b) {
		if(b&1)	{
			res = res * a;
		}
		a = a * a;
		b >>= 1;
	}
	return res;
}

vector < pair < int, int > > getPairs(LL num) {	
	map <int, int> m;
	vector <pair <int, int> > v;
	while(num != 1) {
		m[P[num]]++;
		num /= P[num];
	}
	map <int,int> :: iterator it;
	for(it = m.begin() ; it != m.end() ; it++) {
		v.push_back(make_pair(it->first,it->second));
	}
	return v;
}

void primeSieve() {
	for(int i = 0 ; i < 100005 ; ++i) P[i] = i;
	for(int i = 2 ; i * i < 100005 ; ++i) {
		if(P[i] == i) {
			for(int j = i ; j <= 100005 / i ; ++j) {
				P[i*j] = min(P[i*j],(LL)i);
			}
		}
	}
}

vector<pair<int,int> > getOdd(vector<pair <int,int> > v) {
	vector < pair <int,int> > res;
	for(int i = 0 ; i < v.size() ; ++i) {
		if(v[i].first&1) {
			res.push_back(v[i]);
		}
	}
	return res;
}

LL getSumRecursive(int idx, vector < pair <int,int> > &v) {
	if(idx == v.size())	return 1;
	LL res = 0;
	LL remaining = getSumRecursive(idx + 1, v);
	LL current = getPow(v[idx].first,v[idx].second+1) - 1;
	current /= (v[idx].first - 1);
	res = remaining * current;
	return res;
}

void init() {
	primeSieve();
	A[0] = 0;
	A[1] = 1;
	vector < pair <int,int> > v;
	for(int i = 2 ; i < 100005 ; ++i) {
		v = getPairs(i);
		v = getOdd(v);
		A[i] = getSumRecursive(0,v);
	}
	for(int i = 1 ; i < 100005 ; ++i) A[i] += A[i-1];
}

int main() {
	int t;
	cin >> t;
	int l,r;
	init();
	while(t--) {
		cin >> l >> r;
		cout << A[r] - A[l-1] << endl;
	}
	return 0;
}
