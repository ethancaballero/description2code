#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <vector>
using namespace std;
int a[1005]; //initial colors
int b[1005][1005]; //points associated with each color for each cell
int c[1000][1005]; //penalty points for repainting of each cell with each color
int maxPoints[1005];//max points obtained with or without repainting for each cell
int main() {
	int N, M, K;
	int T;
	scanf("%d", &T);
	while(T--) {
		int ans = 0;
		scanf("%d%d%d", &N, &M, &K);
		for(int i = 0; i < N; i++) {
			scanf("%d", &a[i]);
		}
		for(int i = 0; i < N; i++) {
			for(int j = 0; j < M; j++) {
				scanf("%d", &b[i][j]);
			}
			ans += b[i][a[i]-1];
		}
		for(int i = 0; i < N; i++) {
			for(int j = 0; j < M; j++) {
				scanf("%d", &c[i][j]);
			}
		}
		for(int i = 0; i < N; i++) {
			int temp = 0;
			for(int j = 0; j < M; j++) {
				temp = max(temp, (b[i][j] - b[i][a[i]-1] - c[i][j]));
			}
			maxPoints[i] = temp;
		}
		sort(maxPoints, maxPoints + N);
		reverse(maxPoints, maxPoints + N);
		for(int i = 0; i < K; i++) {
			ans += maxPoints[i];
		}
		cout << ans << endl;
	}
	return 0;
}