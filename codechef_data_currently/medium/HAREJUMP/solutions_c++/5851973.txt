#include<bits/stdc++.h>
#define rep(i, x, n) for(size_t i = x, _n = n; i < _n; i++)
#define lli long long
using namespace std;

typedef vector< lli > row;
typedef vector< row > matrix;

const int MOD = 1e9+7;
	
void clear(matrix &A)	//clears a matrix in O(n^2) time
{
	rep(i, 0, A.size())
		rep(j, 0, A.size())
			A[i][j] = 0;
}

matrix mul(const matrix &A, const matrix &B)	//multiplies 2 matrices in O(n^3) time
{
	matrix C = A;
	clear(C);
	rep(i, 0, C.size())
		rep(j, 0, C[i].size())
			rep(k, 0, A.size())
				C[i][j] = (C[i][j] + A[i][k] * B[k][j])%MOD;
	return C;
}

matrix pow(matrix &A, lli p)	//computes matrix A to the power p in O(log(p)) time
{
	if(p == 0)
	{
		matrix C = A;
		clear(C);
		rep(i, 0, C.size())
			C[i][i] = 1;
		return C;
	}
	matrix C = pow(A, p/2);
	C = mul(C, C);
	if(p&1)
		C = mul(C, A);
	return C;
}

//solves matrix expo for recurrence f(N) = f(N-x1) + f(N-x2) + ...
void solve()
{
	lli N;
	cin >> N;
	const int matrix_size = 16;
	matrix A = matrix(matrix_size, row(matrix_size, 0));

	rep(i, 1, A.size())
		A[i][i - 1] = 1;

	int k, x;
	cin >> k;
	rep(i, 0, k)
	{
		cin >> x;	//f(N) = f(N-x1) + f(N-x2) + ...
		A[0][x - 1] = 1;
	}

	matrix B = pow(A, N);	//compute matrix A to power L
	cout << B[0][0] << endl;//prints N+1'th term of sequence
}

int main()
{
	int t;
	cin >> t;
	while(t--)
	{
		solve();
	}
	return 0;
}
