#include <cstdio>

char M[25005], W[25005];

bool contains(const char *A, const char *B){
	while(*A){
		if(*B==*A)
			B++;
		A++;
	}
	return !*B;
}

int main(){
	int T;
	scanf("%d", &T);
	while(T--){
		scanf("%s %s", M, W);
		puts(contains(M, W) || contains(W, M) ? "YES" : "NO");
	}
	return 0;
}
