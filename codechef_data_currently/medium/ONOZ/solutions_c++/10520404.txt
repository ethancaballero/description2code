using namespace std;

#include "bits/stdc++.h"

bool isValid(int a, int b) {
	if(!a && b || !b && a)	return false;
	int d = a%10;
	while(a) {
		if(a%10 != d)	return false;
		a /= 10;
	}
	while(b) {
		if(b%10 != d)	return false;
		b /= 10;
	}
	return true;
}

int getCount(int h, int m) {
	int res = 0;
	for(int i = 0 ; i < h ; ++i) {
		for(int j = 0 ; j < m ; ++j) {
			if(isValid(i,j)) {
				res++;
			}
		}
	}
	return res;
}

int main() {
	int t;
	int h,m;
	cin >> t;
	while(t--) {
		cin >> h >> m;
		cout << getCount(h,m) << endl;
	}
	return 0;
}
