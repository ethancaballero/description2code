using namespace std;

#include "bits/stdc++.h"

struct node {
	int a,b,c;
};

typedef struct node Node;

int L[105],R[105];

Node N[105];

bool compare(Node N1, Node N2) {
	if(N1.a > N2.a)	return true;
	else if(N1.a < N2.a)	return false;
	if(N1.b > N2.b)	return true;
	else if(N1.b < N2.b)	return false;
	if(N1.c < N2.c)	return true;
	return false;
}

int main() {
	int t;
	int n;
	cin >> t;
	while(t--) {
		cin >> n;
		for(int i = 0 ; i < n ; ++i) 	cin >> L[i];
		for(int i = 0 ; i < n ; ++i)	cin >> R[i];
		for(int i = 0 ; i < n ; ++i) {
			N[i].a = L[i]*R[i];
			N[i].b = R[i];
			N[i].c = i;
		}
		sort(N,N+n,compare);
		cout << N[0].c+1 << endl;
	}
	return 0;
}
