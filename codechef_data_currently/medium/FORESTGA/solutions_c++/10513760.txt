using namespace std;

#include "bits/stdc++.h"

typedef long long LL;

typedef long double LD;

LL INF = 1e18 + 10;

LD currentVal(vector < LD > &v, vector < LD > &g, LD l, LL t) {
	LD res = 0.0;
	for(int i = 0 ; i < v.size() ; ++i) {
		LL curr = v[i] + g[i] * t;
		if(curr >= l) {
			res += curr;
		}
	}
	return res;
}

LL bsearch(LL low, LL high, vector < LD > &v, vector < LD > &g, LD w, LD l) {
	while(low <= high) {
		LD mid = low + (high - low) / 2;
		LD v1 = currentVal(v,g,l,mid);
		if(v1 >= w)	high = mid  - 1;
		else 	low = mid + 1;
	}
	return low;
}

int main() {
	LL n,_w,_l;
	cin >> n >> _w >> _l;
	LD w = _w;
	LD l = _l;
	LL val;
	vector <LD> v(n);
	vector <LD> g(n);
	for(int i = 0 ; i < n ; ++i) {
		cin >> val;
		v[i] = val;
		cin >> val;
		g[i] = val;
	}
	if(currentVal(v,g,l,0) >= w) {
		cout << 0 << endl;
		return 0;
	}
	cout << bsearch(0,1e18+1,v,g,w,l) << endl;
	return 0;
}
