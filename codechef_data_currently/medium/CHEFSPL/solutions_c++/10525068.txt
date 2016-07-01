using namespace std;

#include "bits/stdc++.h"

bool getSpecialEven(string str) {
	int n = str.size();
	for(int i = 0 ; i < n/2 ; ++i) {
		if(str[i] != str[n/2 + i])	return false;
	}
	return true;
}

bool getSpecialOddFirst(string str) {
	int n = str.size();
	if(n == 1)	return false;
	int i = 0;
	int j = n/2;
	int cnt = 0;
	while(i < n/2 && j < n) {
		if(str[i] == str[j]) i++,j++;
		else cnt++,j++;
	}
	return cnt < 2;
}

bool getSpecialOddSecond(string str) {
	int n = str.size();
	if(n == 1)	return false;	
	int i = 0;
	int j = n/2 + 1;
	int cnt = 0;
	while(i <= n/2 && j < n) {
		if(str[i] == str[j]) i++,j++;
		else cnt++,i++;
	}
	return cnt < 2;
}

bool isSpecial(string str) {
	if(!(str.size() & 1)) {
		return getSpecialEven(str);
	} else {
		return getSpecialOddFirst(str) || getSpecialOddSecond(str);
	}
}

int main() {
	int t;
	string str;
	cin >> t;
	while(t--) {
		cin >> str;
		if(isSpecial(str)) puts("YES");
		else puts("NO");
	}
	return 0;
}
