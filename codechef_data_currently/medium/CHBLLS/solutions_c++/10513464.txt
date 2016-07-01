using namespace std;

#include "bits/stdc++.h"

int main() {
	cout << "1" << endl;
	cout << "3 1 1 2" << endl;
	cout << "3 3 3 4" << endl;
	int res;
	cout << flush;
	cin >> res;
	int ans;
	switch(res) {
		case 0 : ans = 5; break;
		case 1 : ans = 2; break;
		case 2 : ans = 1; break;
		case -1 : ans = 4; break;
		case -2 : ans = 3; break;
	}
	cout << "2" << endl;
	cout << ans << endl;	
	return 0;
}